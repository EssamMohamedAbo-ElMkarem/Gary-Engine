import subprocess
import os
import shutil
from Gary.garySE.cfg import config

class yowo():
    def __init__(self, video_path, activity):
        self.video_path = video_path
        self.activity = activity

    def make_dirs(self) -> None:
        """
        This function is used for making the required files in main_dir
        """
        os.chdir(config.main_dir)
        os.mkdir("output_dir")

    def clear_dirs(self) -> None:
        """
        This function is used for clearing the directories
        """
        if not config.flag1:
            if os.path.exists(config.output_dir):
                shutil.rmtree(config.output_dir, ignore_errors=True)

    def detect(self):
        self.clear_dirs()
        self.make_dirs()
        os.chdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "garySE","YOWOv2"))
        if self.activity == 'normal':
            weights = "yowo_v2_tiny_ava_k32.pth"
            type = "ava_v2.2"
        elif self.activity == 'sports':
            weights = "yowo_v2_tiny_ucf24_k32.pth"
            type = "ucf24"

        subprocess.run([config.python_dir + "\\python.exe", 'demo.py', '-d', type, '-v=yowo_v2_tiny',
                        '-size=224', f'--weight={weights}',
                        '--video', self.video_path, '--save_folder', config.output_dir])