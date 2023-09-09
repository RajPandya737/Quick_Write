import pytesseract
from PIL import Image


def ocr(path):
    return pytesseract.image_to_string(
        Image.open(path), lang="eng", config="--psm 6"
    ).replace("\n\x0c", "")


