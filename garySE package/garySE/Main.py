# # from NEW_THREAD_1_VERSION2 import *
# # from NEW_THREAD_2_VERSION2 import *
# from cfg import *
# from THREAD1 import *
# from THREAD2 import *
# import threading
#
# # search
# video_path = "D:\\GarySE\\test.mp4"
# main_class = "person"
# sub_class_value = {'mask': 'with_mask'}
#
# # instantiate objects from each class
# class_1 = Tracking(video_path=video_path, main_class=main_class, scan_rate='quick', trim=False, start=0, end=4000)
# class_2 = Search(video_path=video_path, main_class=main_class, sub_models=sub_class_value, scan_rate='quick',
#                  threshold=12000, p1=(0, 0), p2=(1280, 720))
#
# # class_1.prepare_video()
# # creation of the ma2in 2 threads
# First_Thread = threading.Thread(
#     target=class_1.track, name="Tracking")
# Second_Thread = threading.Thread(target=class_2.search, name="Search")
#
# First_Thread.start()
# Second_Thread.start()
#
# First_Thread.join()
# Second_Thread.join()
#
# print(config.FPS)

from cfg import *
from THREAD1 import *
from THREAD2 import *
import threading


class YOSO(config):
    def __init__(self, video_path: str, main_class: str, sub_models: dict, p1: tuple, p2: tuple, scan_rate: str,
                 trim: bool = False, start: int = 0, end: int = 0, threshold: int = 12000):
        self.video_path = video_path
        self.main_class = main_class
        self.sub_models = sub_models
        self.threshold = threshold
        self.p1 = p1
        self.p2 = p2
        self.scan_rate = scan_rate
        self.trim = trim
        self.start = start
        self.end = end


    def search(self):
        # instantiate objects from each class
        class_1 = Tracking(video_path=self.video_path, main_class=self.main_class, scan_rate=self.scan_rate,
                           trim=self.trim, start=self.start, end=self.end)
        class_2 = Search(video_path=self.video_path, main_class=self.main_class, sub_models=self.sub_models, scan_rate=self.scan_rate,
                         threshold=self.threshold, p1=self.p1, p2=self.p2)

        # class_1.prepare_video()
        # creation of the ma2in 2 threads
        First_Thread = threading.Thread(
            target=class_1.track, name="Tracking")
        Second_Thread = threading.Thread(target=class_2.search, name="Search")

        First_Thread.start()
        Second_Thread.start()

        First_Thread.join()
        Second_Thread.join()

        print(config.FPS)