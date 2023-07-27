"""
This file is used to generate 3-d views based on 2-d images
with different poses and focals extracted in a dataset in the 
form of images, poses and focals encapsulated in numpy arrays.
"""

import os
import cv2
import imageio
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt

# Initialize global variables.
AUTO = tf.data.AUTOTUNE
BATCH_SIZE = 5
NUM_SAMPLES = 32
POS_ENCODE_DIMS = 16
tf.random.set_seed(42)
(num_images, H, W, _) = (0, 0, 0, 0)
poses, focal = None, None



def encode_position(x):
    """Encodes the position into its corresponding Fourier feature.
    Args:
        x: The input coordinate.
    Returns:
        Fourier features tensors of the position.
    """
    positions = [x]
    for i in range(POS_ENCODE_DIMS):
        for fn in [tf.sin, tf.cos]:
            positions.append(fn(2.0**i * x))
    return tf.concat(positions, axis=-1)


def get_rays(height, width, focal, pose):
    """Computes origin point and direction vector of rays.
    Args:
        height: Height of the image.
        width: Width of the image.
        focal: The focal length between the images and the camera.
        pose: The pose matrix of the camera.
    Returns:
        Tuple of origin point and direction vector for rays.
    """
    # Build a meshgrid for the rays.
    i, j = tf.meshgrid(
        tf.range(width, dtype=tf.float32),
        tf.range(height, dtype=tf.float32),
        indexing="xy",
    )

    # Normalize the x axis coordinates.
    transformed_i = (i - width * 0.5) / focal

    # Normalize the y axis coordinates.
    transformed_j = (j - height * 0.5) / focal

    # Create the direction unit vectors.
    directions = tf.stack([transformed_i, -transformed_j, -tf.ones_like(i)], axis=-1)

    # Get the camera matrix.
    camera_matrix = pose[:3, :3]
    height_width_focal = pose[:3, -1]

    # Get origins and directions for the rays.
    transformed_dirs = directions[..., None, :]
    camera_dirs = transformed_dirs * camera_matrix
    ray_directions = tf.reduce_sum(camera_dirs, axis=-1)
    ray_origins = tf.broadcast_to(height_width_focal, tf.shape(ray_directions))

    # Return the origins and directions.
    return (ray_origins, ray_directions)


def render_flat_rays(ray_origins, ray_directions, near, far, num_samples, rand=False):
    """Renders the rays and flattens it.
    Args:
        ray_origins: The origin points for rays.
        ray_directions: The direction unit vectors for the rays.
        near: The near bound of the volumetric scene.
        far: The far bound of the volumetric scene.
        num_samples: Number of sample points in a ray.
        rand: Choice for randomising the sampling strategy.
    Returns:
       Tuple of flattened rays and sample points on each rays.
    """
    # Compute 3D query points.
    # Equation: r(t) = o+td -> Building the "t" here.
    t_vals = tf.linspace(near, far, num_samples)
    if rand:
        # Inject uniform noise into sample space to make the sampling
        # continuous.
        shape = list(ray_origins.shape[:-1]) + [num_samples]
        noise = tf.random.uniform(shape=shape) * (far - near) / num_samples
        t_vals = t_vals + noise

    # Equation: r(t) = o + td -> Building the "r" here.
    rays = ray_origins[..., None, :] + (
        ray_directions[..., None, :] * t_vals[..., None]
    )
    rays_flat = tf.reshape(rays, [-1, 3])
    rays_flat = encode_position(rays_flat)
    return (rays_flat, t_vals)


def map_fn(pose):
    """Maps individual pose to flattened rays and sample points.
    Args:
        pose: The pose matrix of the camera.
    Returns:
        Tuple of flattened rays and sample points corresponding to the
        camera pose.
    """
    (ray_origins, ray_directions) = get_rays(height=H, width=W, focal=focal, pose=pose)
    (rays_flat, t_vals) = render_flat_rays(
        ray_origins=ray_origins,
        ray_directions=ray_directions,
        near=2.0,
        far=6.0,
        num_samples=NUM_SAMPLES,
        rand=True,
    )
    return (rays_flat, t_vals)


def get_nerf_model(num_layers, num_pos):
    """Generates the NeRF neural network.
    Args:
        num_layers: The number of MLP layers.
        num_pos: The number of dimensions of positional encoding.
    Returns:
        The `tf.keras` model.
    """
    inputs = tf.keras.Input(shape=(num_pos, 2 * 3 * POS_ENCODE_DIMS + 3))
    x = inputs
    for i in range(num_layers):
        x = tf.keras.layers.Dense(units=128, activation="relu")(x)
        if i % 4 == 0 and i > 0:
            # Inject residual connection.
            x = tf.keras.layers.concatenate([x, inputs], axis=-1)
    outputs = tf.keras.layers.Dense(units=4)(x)
    return tf.keras.Model(inputs=inputs, outputs=outputs)



def render_rgb_depth(model, rays_flat, t_vals, rand=True, train=True):
    """Generates the RGB image and depth map from model prediction.
    Args:
        model: The MLP model that is trained to predict the rgb and
            volume density of the volumetric scene.
        rays_flat: The flattened rays that serve as the input to
            the NeRF model.
        t_vals: The sample points for the rays.
        rand: Choice to randomise the sampling strategy.
        train: Whether the model is in the training or testing phase.
    Returns:
        Tuple of rgb image and depth map.
    """
    # Get the predictions from the nerf model and reshape it.
    if train:
        predictions = model(rays_flat)
    else:
        predictions = model.predict(rays_flat)
    predictions = tf.reshape(predictions, shape=(BATCH_SIZE, H, W, NUM_SAMPLES, 4))

    # Slice the predictions into rgb and sigma.
    rgb = tf.sigmoid(predictions[..., :-1])
    sigma_a = tf.nn.relu(predictions[..., -1])

    # Get the distance of adjacent intervals.
    delta = t_vals[..., 1:] - t_vals[..., :-1]
    # delta shape = (num_samples)
    if rand:
        delta = tf.concat(
            [delta, tf.broadcast_to([1e10], shape=(BATCH_SIZE, H, W, 1))], axis=-1
        )
        alpha = 1.0 - tf.exp(-sigma_a * delta)
    else:
        delta = tf.concat(
            [delta, tf.broadcast_to([1e10], shape=(BATCH_SIZE, 1))], axis=-1
        )
        alpha = 1.0 - tf.exp(-sigma_a * delta[:, None, None, :])

    # Get transmittance.
    exp_term = 1.0 - alpha
    epsilon = 1e-10
    transmittance = tf.math.cumprod(exp_term + epsilon, axis=-1, exclusive=True)
    weights = alpha * transmittance
    rgb = tf.reduce_sum(weights[..., None] * rgb, axis=-2)

    if rand:
        depth_map = tf.reduce_sum(weights * t_vals, axis=-1)
    else:
        depth_map = tf.reduce_sum(weights * t_vals[:, None, None], axis=-1)
    return (rgb, depth_map)



class NeRF(tf.keras.Model):
    def __init__(self, nerf_model):
        super().__init__()
        self.nerf_model = nerf_model

    def compile(self, optimizer, loss_fn):
        super().compile()
        self.optimizer = optimizer
        self.loss_fn = loss_fn
        self.loss_tracker = tf.keras.metrics.Mean(name="loss")
        self.psnr_metric = tf.keras.metrics.Mean(name="psnr")

    def train_step(self, inputs):
        # Get the images and the rays.
        (images, rays) = inputs
        (rays_flat, t_vals) = rays

        with tf.GradientTape() as tape:
            # Get the predictions from the model.
            rgb, _ = render_rgb_depth(
                model=self.nerf_model, rays_flat=rays_flat, t_vals=t_vals, rand=True
            )
            loss = self.loss_fn(images, rgb)

        # Get the trainable variables.
        trainable_variables = self.nerf_model.trainable_variables

        # Get the gradeints of the trainiable variables with respect to the loss.
        gradients = tape.gradient(loss, trainable_variables)

        # Apply the grads and optimize the model.
        self.optimizer.apply_gradients(zip(gradients, trainable_variables))

        # Get the PSNR of the reconstructed images and the source images.
        psnr = tf.image.psnr(images, rgb, max_val=1.0)

        # Compute our own metrics
        self.loss_tracker.update_state(loss)
        self.psnr_metric.update_state(psnr)
        return {"loss": self.loss_tracker.result(), "psnr": self.psnr_metric.result()}

    def test_step(self, inputs):
        # Get the images and the rays.
        (images, rays) = inputs
        (rays_flat, t_vals) = rays

        # Get the predictions from the model.
        rgb, _ = render_rgb_depth(
            model=self.nerf_model, rays_flat=rays_flat, t_vals=t_vals, rand=True
        )
        loss = self.loss_fn(images, rgb)

        # Get the PSNR of the reconstructed images and the source images.
        psnr = tf.image.psnr(images, rgb, max_val=1.0)

        # Compute our own metrics
        self.loss_tracker.update_state(loss)
        self.psnr_metric.update_state(psnr)
        return {"loss": self.loss_tracker.result(), "psnr": self.psnr_metric.result()}

    @property
    def metrics(self):
        return [self.loss_tracker, self.psnr_metric]



class TrainMonitor(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        loss = logs["loss"]
        loss_list.append(loss)
        test_recons_images, depth_maps = render_rgb_depth(
            model=self.model.nerf_model,
            rays_flat=test_rays_flat,
            t_vals=test_t_vals,
            rand=True,
            train=False,
        )


def get_translation_t(t):
    """Get the translation matrix for movement in t."""
    matrix = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, t],
        [0, 0, 0, 1],
    ]
    return tf.convert_to_tensor(matrix, dtype=tf.float32)



def get_rotation_phi(phi):
    """Get the rotation matrix for movement in phi."""
    matrix = [
        [1, 0, 0, 0],
        [0, tf.cos(phi), -tf.sin(phi), 0],
        [0, tf.sin(phi), tf.cos(phi), 0],
        [0, 0, 0, 1],
    ]
    return tf.convert_to_tensor(matrix, dtype=tf.float32)

def get_rotation_theta(theta):
    """Get the rotation matrix for movement in theta."""
    matrix = [
        [tf.cos(theta), 0, -tf.sin(theta), 0],
        [0, 1, 0, 0],
        [tf.sin(theta), 0, tf.cos(theta), 0],
        [0, 0, 0, 1],
    ]
    return tf.convert_to_tensor(matrix, dtype=tf.float32)

def pose_spherical(theta, phi, t):
    """
    Get the camera to world matrix for the corresponding theta, phi
    and t.
    """
    c2w = get_translation_t(t)
    c2w = get_rotation_phi(phi / 180.0 * np.pi) @ c2w
    c2w = get_rotation_theta(theta / 180.0 * np.pi) @ c2w
    c2w = np.array([[-1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]) @ c2w
    return c2w



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--datapath', type=str, help='Path of the npz dataset with images, poses and focals')
    parser.add_argument('--epochs', type=int, help='Number of epochs')
    opt = parser.parse_args()

    dataset = opt.datapath
    epochs = opt.epochs

    data = np.load(dataset)
    images = data['images']
    (poses, focal) = (data['poses'], data['focal'])
    (num_images, H, W, _) = images.shape
    print(images.shape)


    # Create the training split.
    split_index = int(num_images * 0.8)

    # Split the images into training and validation.
    train_images = images[:split_index]
    val_images = images[split_index:]

    # Split the poses into training and validation.
    train_poses = poses[:split_index]
    val_poses = poses[split_index:]

    # Make the training pipeline.
    train_img_ds = tf.data.Dataset.from_tensor_slices(train_images)
    train_pose_ds = tf.data.Dataset.from_tensor_slices(train_poses)
    train_ray_ds = train_pose_ds.map(map_fn, num_parallel_calls=AUTO)
    training_ds = tf.data.Dataset.zip((train_img_ds, train_ray_ds))
    train_ds = (
        training_ds.shuffle(BATCH_SIZE)
        .batch(BATCH_SIZE, drop_remainder=True, num_parallel_calls=AUTO)
        .prefetch(AUTO)
    )
    # Making the validation pipeline.
    val_img_ds = tf.data.Dataset.from_tensor_slices(val_images)
    val_pose_ds = tf.data.Dataset.from_tensor_slices(val_poses)
    val_ray_ds = val_pose_ds.map(map_fn, num_parallel_calls=AUTO)
    validation_ds = tf.data.Dataset.zip((val_img_ds, val_ray_ds))
    val_ds = (
        validation_ds.shuffle(BATCH_SIZE)
        .batch(BATCH_SIZE, drop_remainder=True, num_parallel_calls=AUTO)
        .prefetch(AUTO)
    )

    test_imgs, test_rays = next(iter(train_ds))
    test_rays_flat, test_t_vals = test_rays
    loss_list = []


    num_pos = H * W * NUM_SAMPLES
    nerf_model = get_nerf_model(num_layers=8, num_pos=num_pos)

    model = NeRF(nerf_model)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(), loss_fn=tf.keras.losses.MeanSquaredError()
    )

    # Create a directory to save the images during training.
    if not os.path.exists("images"):
        os.makedirs("images")

    model.fit(
        train_ds,
        validation_data=val_ds,
        batch_size=BATCH_SIZE,
        epochs=int(epochs),
        callbacks=[TrainMonitor()],
        steps_per_epoch=split_index // BATCH_SIZE,
    )

    nerf_model = model.nerf_model

    rgb_frames = []
    batch_flat = []
    batch_t = []


    for index, theta in tqdm(enumerate(np.linspace(0.0, 360.0, 120, endpoint=False))):
        # Get the camera to world matrix.
        c2w = pose_spherical(theta, -30.0, 4.0)

        
        ray_oris, ray_dirs = get_rays(H, W, focal, c2w)
        rays_flat, t_vals = render_flat_rays(
            ray_oris, ray_dirs, near=2.0, far=6.0, num_samples=NUM_SAMPLES, rand=False
        )

        if index % BATCH_SIZE == 0 and index > 0:
            batched_flat = tf.stack(batch_flat, axis=0)
            batch_flat = [rays_flat]

            batched_t = tf.stack(batch_t, axis=0)
            batch_t = [t_vals]

            rgb, _ = render_rgb_depth(
                nerf_model, batched_flat, batched_t, rand=False, train=False
            )

            temp_rgb = [np.clip(255 * img, 0.0, 255.0).astype(np.uint8) for img in rgb]
            rgb_frames = rgb_frames + temp_rgb
        else:
            batch_flat.append(rays_flat)
            batch_t.append(t_vals)

    rgb_video = "rgb_video.mp4"
    imageio.mimwrite(rgb_video, rgb_frames, fps=30, quality=9, macro_block_size=None)
    print("Saved video to {}".format(rgb_video))
    np_frames = np.asarray(rgb_frames)
    fig = px.imshow(
        np_frames,
        animation_frame=0,
        binary_string=True,
        labels=dict(animation_frame="slice")
    )
    fig.update_layout(title="RGB Reconstruction")
    fig.show()