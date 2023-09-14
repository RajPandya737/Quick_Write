import pytesseract
from PIL import Image


def ocr(path):
    return pytesseract.image_to_string(
        Image.open(path), lang="eng", config="--psm 6"
    ).replace("\n\x0c", "")


def whiteify(path):
    try:
        image = Image.open(path)
        width, height = image.size
        new_image = Image.new("RGBA", (width, height), (255, 255, 255, 255))
        new_image.paste(image, (0, 0), image)
        new_image.save(path)
        image.close()
        new_image.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
