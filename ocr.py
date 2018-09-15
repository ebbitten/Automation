from PIL import Image
import pytesseract
import argparse
import cv2
import os
import imutils
import pyautogui
import numpy as np
import time
from fuzzywuzzy import fuzz
import winsound

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
    # cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    # cv2.waitKey(0)
    return text

def screen_and_compare(text, threshold=80):
    image = takescreenshot()
    ocr_text = ocr(image)
    ratio = fuzz.partial_ratio(text, ocr_text)
    print(ratio)
    if ratio > threshold:
        return True
    else:
        return False


def main():
    phrases = ["Bank Grand Exchange Booth / 23 more options", "Withdraw-1 Green dragonhide / 7 more options", "Close",
             "Cast Tan Leather / 1 more options", "Deposit-1 Green dragon leather / 6 more options"]
    phrases = ["Deposit-1 Green dragon leather / 6 more options"]
    for phrase in phrases:
        print("Starting in 3")
        time.sleep(5)
        image = takescreenshot()
        # cv2.imshow("Image", image)
        # cv2.waitKey(0)
        text = ocr(image)
        print(fuzz.partial_ratio(phrase, text))
        winsound.Beep(2500, 1000)
    winsound.Beep(2000, 2000)


main()


