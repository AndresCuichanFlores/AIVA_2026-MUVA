import re

CONSONANTS  = "BCDFGHJKLMNPQRSTVWXYZ"
VOWELS = "AEIOU"


class PlateValidator:

    def __init__(self):
        self.validated_plates = []

    def validate_plate_format(self, text_plate):
        validate_plate = None
        if len(text_plate) == 1:
            text_result, conf = text_plate[0][1], text_plate[0][2]
            if conf > 0.60:
                text_result = text_result.strip().upper()[-8:]
                if (len(text_result) == 8 and text_result[:4].isdigit() and text_result[4] == " " and
                    len(text_result[5:]) == 3 and all(c in CONSONANTS for c in text_result[5:])
                ):
                    if text_result and text_result not in self.validated_plates:
                        if not self._is_confirmed_plate(text_result):
                            self.validated_plates.append(text_result)
                            validate_plate = text_result
        elif len(text_plate) > 2:
            filtered = [res for res in text_plate if res[2] > 0.50]
            filtered_sorted = sorted(filtered, key=lambda x: x[2], reverse=True)
            text_plate = filtered_sorted[:2]

        if len(text_plate) == 2:
            texts_list, confs_list = [res[1] for res in text_plate], [res[2] for res in text_plate]
            max_conf = max(confs_list)
            if max_conf > 0.90:
                best_text = max(text_plate, key=lambda x: x[2])[1]
                if (len(best_text) == 8 and best_text[:4].isdigit() and best_text[4] == " " and
                    len(best_text[5:]) == 3 and all(c in CONSONANTS for c in best_text[5:])
                ):
                    if best_text and best_text not in self.validated_plates:
                        if not self._is_confirmed_plate(best_text):
                            self.validated_plates.append(best_text)
                            validate_plate = best_text
            if confs_list[0] > 0.60 and confs_list[1] > 0.60:
                text1, text2 = texts_list[0].replace(" ", ""), texts_list[1].replace("|", "")
                text1, text2 = text1.replace("|", "1"), text2.replace("|", "1")
                is_consonants_1 = text1.isalpha() and all(c not in VOWELS for c in text1)
                is_consonants_2 = text2.isalpha() and all(c not in VOWELS for c in text2)
                numbers_part, letters_part = None, None
                if text1.isdigit() and is_consonants_2:
                    numbers_part, letters_part = text1, text2
                elif text2.isdigit() and is_consonants_1:
                    numbers_part, letters_part = text2, text1

                if numbers_part and letters_part:
                    numbers_part_last, letters_part_first = numbers_part[-4:], letters_part[:3]
                    if len(numbers_part_last) == 4 and len(letters_part_first) == 3:
                        text_result = numbers_part_last + " " + letters_part_first.upper()
                        if text_result and text_result not in self.validated_plates:
                            if not self._is_confirmed_plate(text_result):
                                self.validated_plates.append(text_result)
                                validate_plate = text_result
        return validate_plate

    def get_validated_plates(self):
        return self.validated_plates

    def _is_confirmed_plate(self, plate_text):
        prefix6 = plate_text[:6]
        first4 = plate_text[:4]
        last5 = plate_text[-5:]
        exists = any(
            p[:6] == prefix6 or
            p[:4] == first4 or
            p[-5:] == last5
            for p in self.validated_plates
        )
        return exists
