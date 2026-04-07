from ultralytics import YOLO
from pathlib import Path

class LicensePlateDetector:

    def __init__(self):
        model_path = Path(__file__).resolve().parent.parent / "data" / "models" / "best.pt"
        self._model = YOLO(str(model_path))

    def detect_license_plate(self, frame):
        results = self._model(frame, verbose=False)
        result_yolo = results[0]
        return result_yolo

