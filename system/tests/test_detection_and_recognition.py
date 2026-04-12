from src.text_recognizer import TextRecognizer
from src.license_plate_detector import LicensePlateDetector
import cv2
from pathlib import Path

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

# Ubicacion del video
image_test_path = Path(__file__).resolve().parent.parent / "data" / "images" / "image_01.jpg"

def test_detect_license_plate_basic():
    # Instancia del objeto
    detector = LicensePlateDetector()
    # Leemos la imagen de prueba
    img = cv2.imread(str(image_test_path))
    # Comprobación de la imagen
    assert img is not None, "La imagen no se ha cargado"
    # Detectamos matrícula con YOLO
    result = detector.detect_license_plate(img)
    # Comprobación del resultado de YOLO
    assert result is not None
    assert len(result) > 0

def test_recognize_text_basic():
    # Instancia del objeto
    recognizer = TextRecognizer()
    # Leemos la imagen de prueba
    img = cv2.imread(str(image_test_path))
    # Reconocimiento de texto con OCR
    result = recognizer.recognize_text(img)
    # Comprobación del resultado de OCR
    assert result is not None
    assert len(result) > 0

def test_detect_and_recognize_complete():
    # Instancia de los objetos
    detector = LicensePlateDetector()
    recognizer = TextRecognizer()
    # Leemos la imagen de prueba
    img = cv2.imread(str(image_test_path))
    # Detectamos matrícula con YOLO
    result_yolo = detector.detect_license_plate(img)
    # Recortar el bbox
    plate_crop = crop_bbox(img, result_yolo.boxes.xyxy[0], padding_box=0)
    # Preprocesado para OCR
    plate_image = preprocess_for_ocr(plate_crop)
    # Aplicar OCR
    result_text = recognizer.recognize_text(plate_image)

    assert result_text[0][1] == "3049CLG"