# =========================
# IMPORTS
# =========================
import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
from pathlib import Path
import os
from sklearn.cluster import DBSCAN
import random
import os
from ultralytics import YOLO
import easyocr

# =========================
# CONSTANTES
# =========================
PATH_FILE_IMAGES = "../data/images"


# =========================
# FUNCIONES
# =========================
def load_image(filename):
    img_path = PATH_FILE_IMAGES + "/" + filename
    img = cv2.imread(img_path)
    return img

def show_image(img):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()


# =========================
# BLOQUE PRINCIPAL
# =========================
if __name__ == "__main__":

    img = load_image("image_01.jpg")
    show_image(img)

    print(os.getcwd())