from license_plate_detector import LicensePlateDetector
from text_recognizer import TextRecognizer
from plate_validator import PlateValidator
from vehicle_database import VehicleDatabase
import cv2


def crop_bbox(frame, bbox, padding_box):
    x1, y1, x2, y2 = map(int, bbox)
    x1 = max(0, x1 - padding_box)
    y1 = max(0, y1 - padding_box)
    x2 = min(frame.shape[1], x2 + padding_box)
    y2 = min(frame.shape[0], y2 + padding_box)
    plate_crop = frame[y1:y2, x1:x2]
    return plate_crop

def preprocess_for_ocr(plate_crop):
    gray = cv2.cvtColor(plate_crop, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)
    _, plate_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return plate_image


class ALPRSystem:

    def __init__(self):
        self._detector = LicensePlateDetector()
        self._recognizer = TextRecognizer()
        self._validator = PlateValidator()
        self._database = VehicleDatabase()

    def start_system(self, video_path):
        validae = 0
        frame_count = 0
        cap = cv2.VideoCapture(video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            # Solo procesar cada 2 frames
            if frame_count % 2 == 0:
                # Detectar matricula
                result_yolo = self._detector.detect_license_plate(frame)
                # Bucle para reconocer texto de las matriculas
                for bbox, conf in zip(result_yolo.boxes.xyxy, result_yolo.boxes.conf):
                    if conf < 0.50:
                        continue
                    # Recortar el bbox
                    plate_crop = crop_bbox(frame, bbox, padding_box = 0)
                    # Preprocesado para OCR
                    plate_image = preprocess_for_ocr(plate_crop)
                    # Aplicar OCR
                    result_text = self._recognizer.recognize_text(plate_image)
                    # Validar formato matriula
                    validate_plate = self._validator.validate_plate_format(result_text)
                    # Llamar a base de datos
                    if validate_plate:
                        vehicle_info = self._database.query_vehicle(validate_plate)
                        print(f"\nVehicle found in frame {frame_count}:\n{vehicle_info}")
            frame_count += 1
        # Mostrar todas las matriculas validas del video
        print("\nTODAS LAS MATRÍCULAS DEL VIDEO:\n", self._validator.get_validated_plates())
        # Liberamos video
        cap.release()
        cv2.destroyAllWindows()


