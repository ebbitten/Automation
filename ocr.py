from PIL import Image
import pytesseract
import argparse
import cv2
import os
import imutils
import pyautogui
import numpy as np
import time

tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

TEXTBOXY580_E = (0, 22, 320, 35)

def takescreenshot():
    image = pyautogui.screenshot(region=TEXTBOXY580_E)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("screenshot.png", image)
    image = cv2.imread("screenshot.png")
    return image



def ocr(image, preprocess=None):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)
    cv2.imwrite("gray_screenshot.png", gray)
    text = pytesseract.image_to_string(Image.open("gray_screenshot.png"))
    print(text)
    cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    cv2.waitKey(0)


def main():
    print("Starting in 3")
    time.sleep(3)
    image = takescreenshot()
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)
    text = ocr(image)


main()