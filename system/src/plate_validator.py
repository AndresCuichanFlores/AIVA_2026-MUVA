import re

CONSONANTS  = "BCDFGHJKLMNPQRSTVWXYZ"

class PlateValidator:

    def __init__(self):
        self.validated_plates = []

    def validate_plate_format(self, text_plate):
        validate_plate = None
        if len(text_plate) == 1:
            text_result, conf = text_plate[0][1], text_plate[0][2]
            if conf > 0.70:
                text_result = text_result.strip().upper()[-8:]
                if (
                        len(text_result) == 8 and
                        text_result[:4].isdigit() and
                        text_result[4] == " " and
                        len(text_result[5:]) == 3 and
                        all(c in CONSONANTS for c in text_result[5:])
                ):
                    if text_result and text_result not in self.validated_plates:
                        self.validated_plates.append(text_result)
                        validate_plate = text_result
        elif len(text_plate) == 2:
            text_result_1, conf1 = text_plate[0][1], text_plate[0][2]
            text_result_2, conf2 = text_plate[1][1], text_plate[1][2]
            if conf1 > 0.70 and conf2 > 0.70:
                # Solo numeros y 4 digitos
                text_result_2 = re.sub(r'[^0-9]', '', text_result_2)[-4:]
                # Solo consonantes y 3 digitos
                text_result_1 = ''.join(c for c in re.sub(r'[^A-Z]', '', text_result_1.upper()) if c not in "AEIOU")[-3:]
                if len(text_result_2) == 4 and len(text_result_1) == 3:
                    text_result = text_result_2 + " " + text_result_1
                    if text_result and text_result not in self.validated_plates:
                        self.validated_plates.append(text_result)
                        validate_plate = text_result
        return validate_plate

    def get_validated_plates(self):
        return self.validated_plates