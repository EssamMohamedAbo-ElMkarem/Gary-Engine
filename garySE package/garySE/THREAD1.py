"""
This thread is responsible for tracking and generating txt_files which we need for search process
"""
import os
from Gary.garySE.cfg import config
import gc
import subprocess


class Tracking(config):
    def __init__(self, video_path: str, main_class: list, scan_rate: str, trim: bool=False, start: int=0, end: int=0):
        self.video_path = video_path
        self.main_class = main_class
        self.scan_rate = scan_rate
        self.trim = trim
        self.start = start
        self.end = end

    def track(self) -> None:
        if self.scan_rate == 'quick':
            rate = 10
        elif self.scan_rate == 'normal':
            rate = 3
        elif self.scan_rate == 'deep':
            rate = 2
        elif self.scan_rate == 'full':
            rate = 1
        else:
            try:
                Ex = ValueError()
                Ex.strerror = "Wrong value for scan_rate. Please, enter one of these values: quick - normal - deep - full"
                raise Ex
            except ValueError as e:
                print(Ex.strerror)
                os._exit(0)
        os.chdir(config.yolo_dir)
        classes = ''
        for class_ in self.main_class:
            classes = classes + class_ + '::'
        subprocess.run([config.python_dir + "\\python.exe", os.path.join('yolo', 'v8', 'detect', 'detect_and_trk.py'), f'model=yolov8s.pt',
                        f'source={self.video_path}', f'rate={str(rate)}', f'trim={self.trim}', f'start={self.start}',
                        f'end={self.end}', f'classes={classes}'])

        gc.collect()
        config.flag1 = True
