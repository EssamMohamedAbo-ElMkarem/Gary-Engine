# Gary YOLO 🚀, GPL-3.0 license

from pathlib import Path

from Gary.yolo.v8 import classify, detect, segment

ROOT = Path(__file__).parents[0]  # yolov8 ROOT

__all__ = ["classify", "segment", "detect"]

from Gary.yolo.configs import hydra_patch  # noqa (patch hydra cli)
