import sys
import os
import cv2
import pytest

# añadir carpeta src al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from alpr_detection import load_image


def test_load_image_ok():
    img = load_image("image_01.jpg")

    assert img is not None
    assert img.shape[0] > 0
    assert img.shape[1] > 0
    assert len(img.shape) == 3


def test_load_image_not_found():
    with pytest.raises(FileNotFoundError):
        load_image("imagen_que_no_existe.jpg")


def test_image_convert_rgb():
    img = load_image("image_01.jpg")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    assert img_rgb is not None
    assert img_rgb.shape == img.shape


if __name__ == "__main__":
    pytest.main()