"""
This thread is responsible for search process
"""
import os.path
import sys
from Gary.garySE.cfg import config
import gc
import shutil
import numpy as np
import cv2
from moviepy.editor import *
from collections import defaultdict
from keras.models import load_model
from keras import backend as k
from ultralytics import YOLO


class Search(config):
    def __init__(self, video_path: str, main_class: list, sub_models: dict, scan_rate: str, threshold: int=12000,
                 p1: tuple=None, p2: tuple=None, trim: bool=False, start: int=0, end: int=0):
        self.video_path = video_path
        self.sub_models = sub_models
        self.scan_rate = scan_rate
        self.threshold = threshold
        self.p1 = p1
        self.p2 = p2
        self.trim = trim
        self.start = start
        self.end = end
        self.occurrences = defaultdict(list)
        self.not_occurrences = defaultdict(list)
        self.models = [sub_model for sub_model in config.priority if sub_model in self.sub_models.keys()]
        self.step = 0
        self.cnt = 0
        self.thresh_occ = 0
        self.thresh_not_occ = 0
        self.first_model = None
        self.second_model = None
        self.third_model = None
        self.fourth_model = None
        self.fifth_model = None
        self.sixth_model = None
        self.seventh_model = None
        self.eighth_model = None
        self.multiclass_cap = None
        if self.sub_models:
            self.main_class = main_class[0]
        else:
            self.main_class = main_class

    def make_dirs(self) -> None:
        """
        This function is used for making the required files in main_dir
        """
        os.chdir(config.main_dir)
        os.mkdir("save_dir")
        os.mkdir("output_dir")
        with open(f'{config.output_dir}\\TimeStamps.txt', 'w') as f:
            pass

    def clear_dirs(self) -> None:
        """
        This function is used for clearing the directories
        """
        if os.path.exists(config.save_dir):
            shutil.rmtree(config.save_dir, ignore_errors=True)
        if os.path.exists(os.path.join(config.yolo_dir, "runs")):
            os.chdir(config.yolo_dir)
            shutil.rmtree("runs", ignore_errors=True)
        if not config.flag1:
            if os.path.exists(config.output_dir):
                shutil.rmtree(config.output_dir, ignore_errors=True)

    def pipeline(self, image) -> np.ndarray:
        """
        This function is a pipeline for the image processing before feeding it to the model
            resize the image to 256x256 and normalize it
            expand dims to make the image compatible with the model "batches"
        args:
            images_path: the path of the images' folder
        return:
            img : the processed image (1, 256, 256, nc)
        """
        img = cv2.resize(image,
                         (256, 256)).astype(np.float32) / 255.0
        img = np.expand_dims(img, axis=0)
        return img

    def get_step(self) -> None:
        """
        This function is used to get the step which means number of frames which will be ignored by YOLO and
        search algorithm according to scan_rate.
        It also used to get minimum number of occurrences to consider this object as an occurrence in txt file
        """
        if self.scan_rate == 'quick':
            self.step = 9
            self.cnt = self.step + 1
            self.thresh_occ = config.FPS / 10
            self.thresh_not_occ = 3
        elif self.scan_rate == 'normal':
            self.step = 2
            self.cnt = self.step + 1
            self.thresh_occ = config.FPS / 3
            self.thresh_not_occ = 7
        elif self.scan_rate == 'deep':
            self.step = 1
            self.cnt = self.step + 1
            self.thresh_occ = config.FPS / 2
            self.thresh_not_occ = 10
        elif self.scan_rate == 'full':
            self.thresh_occ = config.FPS / 1
            self.thresh_not_occ = 15
        else:
            try:
                Ex = ValueError()
                raise Ex
            except ValueError as e:
                os._exit()

    def LoadModel(self, model_name: str):
        if model_name not in ['clothes', 'colors']:
            model = load_model(config.models_paths[model_name])
        else:
            if model_name == 'clothes':
                model = YOLO(os.path.join(config.main_dir, "models\\Persons\\clothes\\clothes.pt"))

        return model

    def load_models(self) -> None:
        try:
            self.first_model = self.LoadModel(self.models[0])
            self.second_model = self.LoadModel(self.models[1])
            self.third_model = self.LoadModel(self.models[2])
            self.fourth_model = self.LoadModel(self.models[3])
            self.fifth_model = self.LoadModel(self.models[4])
            self.sixth_model = self.LoadModel(self.models[5])
            self.seventh_model = self.LoadModel(self.models[6])
            self.eighth_model = self.LoadModel(self.models[7])
        except:
            if 'hat' in self.models:
                if self.sub_models["hat"] != "without_cap":
                    self.multiclass_cap = load_model(config.multiclass_hat_path)

    def select_model(self, model_number):
        model = None
        if model_number == 0:
            model = self.first_model
        elif model_number == 1:
            model = self.second_model
        elif model_number == 2:
            model = self.third_model
        elif model_number == 3:
            model = self.fourth_model
        elif model_number == 4:
            model = self.fifth_model
        elif model_number == 5:
            model = self.sixth_model
        elif model_number == 6:
            model = self.seventh_model
        elif model_number == 7:
            model = self.eighth_model
        return model

    def predict(self, i, object_):
        model = self.select_model(i)
        if self.models[i] not in ["hat", "clothes", "colors"]:
            object_ = self.pipeline(object_)
            prediction = np.argmax(model.predict(object_))
            if prediction != config.mapping[self.models[i]][self.sub_models[self.models[i]]]:
                return False
            else:
                return True

        elif self.models[i] == "hat":
            object_ = self.pipeline(object_)
            prediction = np.argmax(model.predict(object_))
            if self.sub_models["hat"] == "without_cap":
                if prediction == 1:
                    return True
                else:
                    return False
            else:
                if prediction == 0:
                    cap_mapping = {'cap': 0, 'capuchon': 1, 'helmet': 2, 'hijab': 3, 'icecap': 4}
                    CapType = np.argmax(self.multiclass_cap.predict(object_))
                    if CapType == cap_mapping[self.sub_models["hat"]]:
                        return True
                    else:
                        return False
                else:
                    return False

        elif self.models[i] == "clothes":
            # image preprocessing as model specifications and training data
            img = cv2.resize(object_, (640, 640), cv2.INTER_AREA)

            # prediction
            results = model.predict(img, conf=0.45, iou=0.45)
            output_classes = results[0].boxes.cls.tolist()
            output_classes = [int(output_classes[i]) for i in range(len(output_classes))]
            output_classes = [config.Index2Cloth[output] for output in output_classes]

            if self.sub_models["clothes"] in output_classes:
                return True
            else:
                return False

    def generate_video(self) -> None:
        """
        This function is used for generating the video
        """
        os.chdir(config.save_dir)

        os.chdir(config.output_dir)
        video = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'),
                                config.FPS, (config.width, config.height))

        # Appending the images to the video one by one
        for i in range(1, len(os.listdir(config.save_dir)) + 1):
            video.write(cv2.imread(os.path.join(
                config.save_dir, "Frame" + str(i) + ".jpg")))

        # Deallocating memories taken for window creation
        cv2.destroyAllWindows()
        video.release()

    def generate_occurrences(self, occurrences: dict) -> None:
        """
        This function is used for getting the time of each frame
        args:
            frame: the name of the frame
            frame_number: the number of the frame
        output:
            appending the time of each frame text file "TimeStamps.txt"
        """
        i = 1
        for occ, frames in occurrences.items():
            if len(frames) < self.thresh_occ:
                continue

            start_frame = min(frames)
            end_frame = max(frames)
            start_time = float(start_frame / config.FPS)
            end_time = float(end_frame / config.FPS)

            # print(occ, frames,"start frame is", start_frame,"end frame is", end_frame)

            with open(f'{config.output_dir}\\TimeStamps.txt', 'a') as f:
                f.write(f'Occurrence_{i} {str(round(start_time, 2))} {str(round(end_time, 2))}\n')

            for j in range(start_frame, end_frame+1, self.step+1):
                # print("j = ", j)
                if os.path.exists(os.path.join(config.yolo_dir, 'runs', 'detect', 'train', 'labels', f'Frame{j}.txt')):
                    img = cv2.imread(os.path.join(config.save_dir, 'Frame' + str(j) + '.jpg'))
                    with open(
                            os.path.join(config.yolo_dir, 'runs', 'detect', 'train', 'labels', f'Frame{j}.txt')) as f:
                        lines = f.readlines()
                        for line in lines:
                            # print(line.split()[0], str(occ))
                            if str(line.split()[0]) == str(occ):
                                cv2.rectangle(img,
                                              (int(float(line.split()[2])), int(float(line.split()[3]))),
                                              (int(float(line.split()[4])), int(float(line.split()[5]))),
                                              (0, 255, 0), 2)

                                cv2.imwrite(os.path.join(config.save_dir, f'Frame{j}.jpg'), img)

            i += 1

    def search(self):
        self.clear_dirs()
        self.make_dirs()

        # Opens the Video file
        cap = cv2.VideoCapture(self.video_path)
        # Get the video's width, height and FPS
        config.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        config.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        config.FPS = cap.get(cv2.CAP_PROP_FPS)

        if self.p1 == None:
            self.p1 = (0, 0)
        if self.p2 == None:
            self.p2 = (config.width, config.height)

        self.get_step()

        if len(self.models) != 0:
            self.load_models()

        while True:
            if os.path.exists(os.path.join(config.yolo_dir, 'runs', 'detect', 'train', 'labels')) and \
                    len(os.listdir(os.path.join(config.yolo_dir, 'runs', 'detect', 'train', 'labels'))) != 0:
                break

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                gc.collect()
                break

            if self.trim:
                if config.frame_number > self.end * config.FPS:
                    gc.collect()
                    break
                elif config.frame_number < self.start * config.FPS:
                    config.frame_number += 1
                    continue

            while len(os.listdir(os.path.join(config.yolo_dir, 'runs', 'detect', 'train', 'labels'))) <= \
                    round(len(os.listdir(config.save_dir))/(self.step+1)) and not config.flag1:
                gc.collect()
                continue

            # Save images
            cv2.imwrite(os.path.join(config.save_dir, 'Frame' +
                                     str(config.frame_number) + '.jpg'), frame)

            if self.cnt == self.step + 1 or self.step == 0:
                self.cnt -= 1
                config.done += 1

                if not (
                        os.path.exists(
                            os.path.join(os.path.join(config.yolo_dir, "runs\\detect\\train\\labels",
                                         f'Frame{config.frame_number}.txt')))):
                    config.frame_number += 1
                    continue

                # Prepare the original image and get its width and height
                img = cv2.imread(os.path.join(config.save_dir, 'Frame' + str(config.frame_number) + '.jpg'))

                with open(
                        os.path.join(os.path.join(config.yolo_dir, "runs\\detect\\train\\labels",
                                                  f'Frame{config.frame_number}.txt'))) as f:
                    lines = f.readlines()
                    if len(self.models) != 0:
                        for line in lines:
                            if len(self.not_occurrences[line.split()[0]]) > self.thresh_not_occ:
                                continue

                            # if line.split()[1] != config.Class2Index[self.main_class]:
                            #     continue
                            width = int(float(line.split()[4])) - int(float(line.split()[2]))
                            height = int(float(line.split()[5])) - int(float(line.split()[3]))
                            x_center = int(float(line.split()[2])) + (width / 2)
                            y_center = int(float(line.split()[3])) + (height / 2)

                            if not ((x_center > self.p1[0]) and (x_center < self.p2[0]) and (
                                    y_center > self.p1[1]) and (y_center < self.p2[1])):
                                continue

                            object_ = img[abs(int(float(line.split()[3]))):abs(int(float(line.split()[5]))),
                                          abs(int(float(line.split()[2]))):abs(int(float(line.split()[4]))),
                                          :]
                            if (object_.shape[0] * object_.shape[1]) < self.threshold:
                                continue

                            for j in range(len(self.models)):
                                check = self.predict(j, object_)
                                if not check:
                                    self.not_occurrences[line.split()[0]].append(config.frame_number)
                                    break

                                if check and (j == len(self.models) - 1):
                                    self.occurrences[line.split()[0]].append(config.frame_number)

                    else:
                        for line in lines:
                            width = int(float(line.split()[4])) - int(float(line.split()[2]))
                            height = int(float(line.split()[5])) - int(float(line.split()[3]))
                            x_center = int(float(line.split()[2])) + (width / 2)
                            y_center = int(float(line.split()[3])) + (height / 2)

                            if not ((x_center > self.p1[0]) and (x_center < self.p2[0]) and (
                                    y_center > self.p1[1]) and (y_center < self.p2[1])):
                                continue

                            object_ = img[abs(int(float(line.split()[3]))):abs(int(float(line.split()[5]))),
                                      abs(int(float(line.split()[2]))):abs(int(float(line.split()[4]))),
                                      :]
                            if (object_.shape[0] * object_.shape[1]) < self.threshold:
                                continue

                            self.occurrences[line.split()[0]].append(config.frame_number)


            else:
                self.cnt -= 1
                if self.cnt <= 0:
                    self.cnt = self.step + 1

            config.frame_number += 1

            if config.done % 10000 == 0:
                k.clear_session()
                gc.collect()
                self.load_models()

        self.generate_occurrences(self.occurrences)
        self.generate_video()
        self.clear_dirs()
