import cv2
import numpy as np
from PIL import Image
from scipy.ndimage import interpolation as inter


class ScannedImage:
    def __init__(self, path):
        self.path = path
        self.img = cv2.imread(path)

    def invert(self):
        self.img = cv2.bitwise_not(self.img)

    def grayscale(self):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        return self.img

    def binarize(self, threshold=127):
        self.img = cv2.threshold(
            self.grayscale(), threshold, 200, cv2.THRESH_BINARY)[1]

    def noise_removal(self, shape=1):
        kernal = np.ones((shape, shape), np.uint8)
        self.img = cv2.dilate(self.img, kernal, iterations=1)
        kernal = np.ones((shape, shape), np.uint8)
        self.img = cv2.erode(self.img, kernal, iterations=1)
        self.img = cv2.morphologyEx(self.img, cv2.MORPH_OPEN, kernal)
        self.img = cv2.medianBlur(self.img, 3)

    def getSkewAngle(self, cvImage) -> float:
        newImage = cvImage.copy()
        gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (9, 9), 0)
        thresh = cv2.threshold(
            blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
        dilate = cv2.dilate(thresh, kernel, iterations=2)
        contours, hierarchy = cv2.findContours(
            dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        for c in contours:
            rect = cv2.boundingRect(c)
            x, y, w, h = rect
            cv2.rectangle(newImage, (x, y), (x+w, y+h), (0, 255, 0), 2)
        largestContour = contours[0]
        print(len(contours))
        minAreaRect = cv2.minAreaRect(largestContour)
        cv2.imwrite("temp/boxes.jpg", newImage)
        angle = minAreaRect[-1]
        if angle < -45:
            angle = 90 + angle
        return -1.0 * angle

    def rotateImage(self, cvImage, angle: float):
        newImage = cvImage.copy()
        (h, w) = newImage.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        newImage = cv2.warpAffine(
            newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return newImage

    def change_font(self, shape=2, font_size=True):
        # if font_size is True, then enlarge the font, else shrink
        self.img = cv2.bitwise_not(self.img)
        kernal = np.ones((shape, shape), np.uint8)
        if font_size:
            self.img = cv2.dilate(self.img, kernal, iterations=1)
        else:
            self.img = cv2.erode(self.img, kernal, iterations=1)
        self.img = cv2.bitwise_not(self.img)

    def deskew(self):
        angle = self.getSkewAngle(self.img)
        self.img = self.rotateImage(self.img, -1.0 * angle)
    
    def remove_border(self):
        contours, hierarchy = cv2.findContours(self.img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cntSorted = sorted(contours, key=lambda x: cv2.contourArea(x))
        cnt = cntSorted[-1]
        x, y, w, h = cv2.boundingRect(cnt)
        crop = self.img[y:y+h, x:x+w]
        self.img = crop

    def add_border(self, border_size=100):
        color = [255, 255, 255]
        top, bottom, left, right = [border_size]*4
        image_with_border = cv2.copyMakeBorder(self.img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
        self.img = image_with_border
    
    def show(self):
        cv2.imshow("Image", self.img)
        cv2.waitKey(0)
    
    def save(self, path):
        cv2.imwrite(path, self.img)

if __name__ == "__main__":
    scanned_image = ScannedImage("static/drawings/img1.jpg")
    scanned_image.process()

