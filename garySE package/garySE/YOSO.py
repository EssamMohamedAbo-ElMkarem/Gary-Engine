import os
import threading
from transformers import pipeline
from Gary.garySE.cfg import config
from Gary.garySE.THREAD1 import *
from Gary.garySE.THREAD2 import *
from Gary.garySE.T5Transformer import T5Transformer


class yoso(config):
    def __init__(self, video_path: str, main_class: list, text: str = '', scan_rate: str = 'quick',
                 search_type: str = 'smart', p1: tuple = None, p2: tuple = None, trim: bool = False,
                 start: int = 0, end: int = 0, threshold: int = 12000):
        self.video_path = video_path
        self.text = text
        self.main_class = main_class
        self.scan_rate = scan_rate
        self.search_type = search_type
        self.p1 = p1
        self.p2 = p2
        self.trim = trim
        self.start = start
        self.end = end
        self.threshold = threshold

    def search(self):
        mapping = {}

        for class_ in self.main_class:
            if class_ not in config.classes:
                try:
                    Ex = ValueError()
                    Ex.strerror = f"main_class must be one of these classes: {config.classes}"
                    raise Ex
                except ValueError as e:
                    print(Ex.strerror)
                    os._exit(0)

        if self.text != '':
            if self.search_type.lower() == 'smart':
                translator = pipeline("translation", model=os.path.join(config.main_dir, "models\\Search_Bar\\Translation"))
                text = translator(self.text)
                print(text)
                output = T5Transformer(text[0]['translation_text']).get_classes()

                for part in output.split(","):
                    if part.split(":")[1] != 'None':
                        mapping[(part.split(":")[0]).lower()] = (part.split(":")[1]).lower()

            elif self.search_type.lower() == 'original':
                for part in self.text.split(","):
                    if part.split(":")[1] != 'None':
                        mapping[(part.split(":")[0]).lower()] = (part.split(":")[1]).lower()

            else:
                try:
                    Ex = ValueError()
                    Ex.strerror = "search_type must be original or smart"
                    raise Ex
                except ValueError as e:
                    print(Ex.strerror)
                    os._exit(0)

        print(mapping)

        # instantiate objects from each class
        class_1 = Tracking(video_path=self.video_path, main_class=self.main_class, scan_rate=self.scan_rate,
                           trim=self.trim, start=self.start, end=self.end)
        class_2 = Search(video_path=self.video_path, main_class=self.main_class, sub_models=mapping, scan_rate=self.scan_rate,
                         threshold=self.threshold, p1=self.p1, p2=self.p2, trim=self.trim, start=self.start, end=self.end)

        # creation of the ma2in 2 threads
        First_Thread = threading.Thread(target=class_1.track, name="Tracking")
        Second_Thread = threading.Thread(target=class_2.search, name="Search")

        First_Thread.start()
        Second_Thread.start()

        First_Thread.join()
        Second_Thread.join()
