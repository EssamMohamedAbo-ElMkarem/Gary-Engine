import subprocess
import shutil
# Normal
# Quick
# Full
x = 'Normal'
# x = 10


if x == 'Deep':
    subprocess.run(['cmd', '/c', 'python', 'yolo\\v8\detect' + '\detect_and_trk.py', 'model=yolov8s.pt',
                    'source=street.mp4', 'rate=2', 'trim=True', 'start=1', 'end=5'])
elif x == 'Full':
    subprocess.run(['cmd', '/c', 'python', 'yolo\\v8\detect' + '\detect_and_trk.py', 'model=yolov8s.pt',
                    'source=street.mp4', 'rate=1', 'trim=True', 'start=1', 'end=5'])
elif x == 'Normal':
    subprocess.run(['cmd', '/c', 'python', 'yolo\\v8\detect' + '\detect_and_trk.py', 'model=yolov8s.pt',
                    'source=street.mp4', 'rate=3', 'trim=False', 'start=1', 'end=5'])
elif x == 'Quick':
    subprocess.run(['cmd', '/c', 'python', 'yolo\\v8\detect' + '\detect_and_trk.py', 'model=yolov8s.pt',
                    'source=street.mp4', 'rate=10', 'trim=True', 'start=0', 'end=300'])

# subprocess.run(['cmd', '/c', 'python', 'yolo\\v8\detect' + '\detect_and_trk.py', 'model=yolov8s.pt',
#                 'source=street.mp4', "rate=" + str(x), 'trim=True', 'start=1', 'end=5',
#                 'project=' + r"C:\Users\Amr\Desktop\outputs"])
