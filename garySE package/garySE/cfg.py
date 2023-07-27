"""
this file contains all the configurations :
- global queues:
    - q1: for the frames
    - q2: for raising the flag in VSE_thread3.py
- paths
- lists
- dictionaries
- maps
"""
import os.path
import os
# os.chdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "garySE"))


class config:
    # os.chdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "garySE"))

    flag1 = False

    # defining variables
    FPS = 0
    height = 0
    width = 0

    frame_number = 1
    done = 0

    # the directory of the folder which contains everything
    main_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "garySE")
    # the directory saved from FramesToImage Class
    save_dir = os.path.join(main_dir, "save_dir")
    # the directory for our main python interpreter
    python_dir = '\\'.join(os.path.dirname(os.path.abspath(__file__)).split('\\')[:-4])
    # the directory of YOLO repo which we have cloned
    yolo_dir = os.path.join(main_dir, "tracking")
    # the directory which the output video will be saved in
    output_dir = os.path.join(main_dir, "output_dir")

    # create empty txt file to contain time stamps
    # with open(f'{output_dir}\\TimeStamps.txt', 'w') as f:
    #     pass

    # defining yolo v7 classes
    classes = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
               'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
               'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
               'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
               'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard',
               'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase',
               'scissors', 'teddy bear', 'hair drier', 'toothbrush']

    # defining dictionary to map each class to its index
    Class2Index = {'person': '0', 'bicycle': '1', 'car': '2', 'motorcycle': '3', 'airplane': '4', 'bus': '5',
                   'train': '6', 'truck': '7', 'boat': '8', 'traffic light': '9',
                   'fire hydrant': '10', 'stop sign': '11', 'parking meter': '12', 'bench': '13', 'bird': '14',
                   'cat': '15', 'dog': '16', 'horse': '17', 'sheep': '18',
                   'cow': '19', 'elephant': '20', 'bear': '21', 'zebra': '22', 'giraffe': '23', 'backpack': '24',
                   'umbrella': '25', 'handbag': '26', 'tie': '27',
                   'suitcase': '28', 'frisbee': '29', 'skis': '30', 'snowboard': '31', 'sports ball': '32',
                   'kite': '33', 'baseball bat': '34', 'baseball glove': '35',
                   'skateboard': '36', 'surfboard': '37', 'tennis racket': '38', 'bottle': '39', 'wine glass': '40',
                   'cup': '41', 'fork': '42', 'knife': '43',
                   'spoon': '44', 'bowl': '45', 'banana': '46', 'apple': '47', 'sandwich': '48', 'orange': '49',
                   'broccoli': '50', 'carrot': '51', 'hot dog': '52',
                   'pizza': '53', 'donut': '54', 'cake': '55', 'chair': '56', 'couch': '57', 'potted plant': '58',
                   'bed': '59', 'dining table': '60', 'toilet': '61',
                   'tv': '62', 'laptop': '63', 'mouse': '64', 'remote': '65', 'keyboard': '66', 'cell phone': '67',
                   'microwave': '68', 'oven': '69', 'toaster': '70',
                   'sink': '71', 'refrigerator': '72', 'book': '73', 'clock': '74', 'vase': '75', 'scissors': '76',
                   'teddy bear': '77', 'hair drier': '78', 'toothbrush': '79'}

    Index2Cloth = {0: 'Bag', 1: 'Dress', 2: 'Hijab', 3: 'Hoodie', 4: 'Jacket', 5: 'Pant', 6: 'Shirt', 7: 'Short',
                   8: 'Skirt', 9: 'Suit', 10: 'T-shirt'}

    Index2Char = {"9": "أ", "16": "ق", "11": "ب", "22": "ص", "21": "س", "23": "ط", "10": "ع", "17": "ل", "20": "ر",
                  "19": "ن", "18": "م", "15": "ه", "24": "و", "25": "ى", "14": "ج", "12": "د", "13": "ف", "0": "١",
                  "1": "٢", "2": "٣", "3": "٤", "4": "٥", "5": "٦", "6": "٧", "7": "٨", "8": "٩"}

    # defining relative paths for sub-models
    mask_path = os.path.join(main_dir, "models\\Persons\\masks\\mask_detection_model.h5")
    avg_age_path = os.path.join(main_dir, "models\\Persons\\avg_age\\Average_age_detector.h5")
    gender_path = os.path.join(main_dir, "models\\Persons\\gender\\gender_new_detector.h5")
    binary_hat_path = os.path.join(main_dir, "models\\Persons\\hats\\binary_hat_detection_model.h5")
    multiclass_hat_path = os.path.join(main_dir, "models\\Persons\\hats\\multi_hat_detection_model.h5")
    glasses_path = os.path.join(main_dir, "models\\Persons\\glasses\\glasses_detection_model.h5")
    color_path = os.path.join(main_dir, "models\\Cars\\color\\color_detector.h5")
    car_type_path = os.path.join(main_dir, "models\\Cars\\car_type\\cartype_model.h5")
    plates_no_paths = os.path.join(main_dir, "models\\Cars\\plates_no\\plates_no_detector.h5")

    # defining the features dictionaries for person
    models_paths = {
        'avg_age': avg_age_path,
        'gender': gender_path,
        'hat': binary_hat_path,
        'Glasses': glasses_path,
        'mask': mask_path,
        'color': color_path,
        'plates_no': plates_no_paths,
        'car_type': car_type_path
    }

    # PERSONS_FEATURES = {
    #     'avg_age': avg_age_path,
    #     'gender': gender_path,
    #     'hat': binary_hat_path,
    #     'glasses': glasses_path,
    #     'mask': mask_path
    # }
    #
    # # defining the features dictionaries for car
    # CAR_FEATURES = {
    #     'color': color_path,
    #     'plates_no': plates_no_paths
    # }

    # defining the mapping for the features
    # mapping the sub-model and its value to the prediction
    mapping = {
        # 'hat': {'cap': 0, 'capuchon': 1, 'helmet': 2, 'hijab': 3, 'icecap': 4},
        # 'hat': {'cap': 0, 'capuchon': 0, 'helmet': 0, 'hijab': 0, 'icecap': 0, 'without_cap': 1},
        'Glasses': {'with_glasses': 0, 'without_glasses': 1},
        'avg_age': {'old': 0, 'young': 1, 'youth': 2},
        'mask': {'with_mask': 0, 'without_mask': 1},
        'gender': {'female': 0, 'male': 1},
        'car_type': {'van': 0, 'suv': 1, 'other': 2, 'minivan': 3, 'cab': 4, 'wagon': 5, 'sedan': 6, 'hatchback': 7, 'coupe': 8, 'convertible': 9}
    }

    priority = ['mask', 'gender', 'Glasses', 'hat', 'avg_age', 'clothes', 'color']
