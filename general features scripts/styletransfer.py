"""
This file is used to apply style trasfer from a style image
into a content image and the combination image shall be displayed
using a matplotlib plot.
"""

import argparse
import cv2
import numpy as np
import tensorflow as tf
from datetime import datetime
from matplotlib import pyplot as plt


def gram_matrix(x):
    """
    Gram matrix
    :param x:
    :return gram matrix
    """
    x = tf.transpose(x, (2, 0, 1))
    features = tf.reshape(x, (tf.shape(x)[0], -1))
    gram = tf.matmul(features, tf.transpose(features))
    return gram

def style_cost(style, combination):
    """
    Style cost function
    :param style: style image
    :param combination: combination image
    :return: style cost
    """
    S = gram_matrix(style)
    C = gram_matrix(combination)
    channels = 3
    size = W * H
    return tf.reduce_sum(tf.square(S - C)) / (4.0 * (channels ** 2) * (size ** 2))

def content_cost(content, combination):
    """
    Content cost function
    :param content: content image
    :param combination: combination image
    :return: content cost
    """
    return tf.reduce_sum(tf.square(combination - content))

def loss_function(combination_image, base_image, style_reference_image):
    """
    Loss function
    :param combination_image: combination image
    :param base_image: base image
    :param style_reference_image: style reference image
    :return: total cost
    """
    # 1. Combine all the images in the same tensioner.
    input_tensor = tf.concat(
        [base_image, style_reference_image, combination_image], axis=0
    )

    # 2. Get the values in all the layers for the three images.
    features = feature_extractor(input_tensor)

    #3. Inicializar the loss

    loss = tf.zeros(shape=())

    # 4. Extract the content layers + content loss
    layer_features = features[cap_content]
    base_image_features = layer_features[0, :, :, :]
    combination_features = layer_features[2, :, :, :]

    loss = loss + content_weight * content_cost(
        base_image_features, combination_features
    )
    # 5. Extraer the style layers + style loss
    for layer_name in cap_style:
        layer_features = features[layer_name]
        style_reference_features = layer_features[1, :, :, :]
        combination_features = layer_features[2, :, :, :]
        sl = style_cost(style_reference_features, combination_features)
        loss += (style_weight / len(cap_style)) * sl

    return loss


@tf.function
def compute_loss_and_grads(combination_image, base_image, style_reference_image):
    """
    Compute the loss and the gradients
    :param combination_image: combination image
    :param base_image: base image
    :param style_reference_image: style reference image
    :return: computes the loss and gradients
    """
    with tf.GradientTape() as tape:
        loss = loss_function(combination_image, base_image, style_reference_image)
    grads = tape.gradient(loss, combination_image)
    return loss, grads


def preprocess_image(image_path):
    # Util function to open, resize and format pictures into appropriate tensors
    img = cv2.resize(image_path, (W, H))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.vgg19.preprocess_input(img)
    return tf.convert_to_tensor(img)


def deprocess_image(x):

    x = x.reshape((W, H, 3))

    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68

    x = x[:, :, ::-1]

    x = np.clip(x, 0, 255).astype("uint8")

    return x


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--content', nargs='+', type=str, help='content image')
    parser.add_argument('--style', type=str, help='style image') 
    parser.add_argument('--epochs', type=int, help='epochs number') 
    opt = parser.parse_args()

    content_path = opt.content[0]
    style_path = opt.style
    epochs = opt.epochs
    print(content_path)
    print(style_path)
    print(epochs)
    content = plt.imread(content_path)
    style = plt.imread(style_path)
    W, H = content.shape[1], content.shape[0]

    model = tf.keras.applications.vgg19.VGG19(weights='imagenet', include_top=False)
    outputs_dict= dict([(layer.name, layer.output) for layer in model.layers])
    feature_extractor = tf.keras.Model(inputs=model.inputs, outputs=outputs_dict)
    cap_style = [
        "block1_conv1",
        "block2_conv1",
        "block3_conv1",
        "block4_conv1",
        "block5_conv1",
    ]

    cap_content = "block5_conv2"

    content_weight = 2.5e-8
    style_weight = 1e-6

    img_nrows = W
    img_ncols = H
    optimizer = tf.keras.optimizers.Adam(
        tf.keras.optimizers.schedules.ExponentialDecay(
            initial_learning_rate=0.5, decay_steps=10, decay_rate=0.96
        )
    )

    base_image = preprocess_image(content)
    style_reference_image = preprocess_image(style*255)
    combination_image = tf.Variable(preprocess_image(content))


    for j in range(1, int(epochs) + 1):
        loss, grads = compute_loss_and_grads(
            combination_image, base_image, style_reference_image
        )
        optimizer.apply_gradients([(grads, combination_image)])
        if j % 10 == 0:
            print("Iteration %d: loss=%.2f" % (j, loss))
    img = deprocess_image(combination_image.numpy())
    plt.imshow(img)