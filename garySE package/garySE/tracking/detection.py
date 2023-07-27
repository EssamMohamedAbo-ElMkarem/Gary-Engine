from Gary import YOLO
#ultralytics
model = YOLO("yolov8s.pt")
model.predict(source="street.mp4", conf=0.25, hide_labels=True, save=True)
