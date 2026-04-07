import easyocr

class TextRecognizer:

    def __init__(self):
        self._reader = easyocr.Reader(['en'], gpu=True)

    def recognize_text(self, plate_image):
        result_text = self._reader.readtext(plate_image, detail=1)
        return result_text