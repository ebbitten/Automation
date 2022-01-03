import time
import subprocess
from PIL import Image
import pytesseract
from fuzzywuzzy import fuzz
from operator import itemgetter
import cv2
import numpy as np
import pyautogui
import platform

from assets import coordinates
from ocr_lib import *


is_retina = False
if platform.system() == "Darwin":
    is_retina = subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True)



TEXTBOXY580_E = (70, 50, 400, 20)


def takescreenshot(region=TEXTBOXY580_E, file_path="screenshot.png"):
    image = pyautogui.screenshot(region=region)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("screenshot.png", image)
    image = cv2.imread("screenshot.png")
    return image

def ocr(image, preprocess=["thresh"]):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if "blur" in preprocess:
        gray = cv2.medianBlur(gray, 3)
    if "thresh" in preprocess:
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imwrite("gray_screenshot.png", gray)
    text = pytesseract.image_to_string(Image.open("gray_screenshot.png"))
    print(text)
    # cv2.imshow("Image", image)
    # cv2.imshow("Output", gray)
    # cv2.waitKey(0)
    return text, gray

def screen_and_compare(text, threshold=60, take_failed_screenshot=False, region=TEXTBOXY580_E):
    image = takescreenshot(region)
    ocr_text, image = ocr(image)
    ratio = fuzz.partial_ratio(text, ocr_text)
    print("ratio is ", ratio)
    print("original text was ", text)
    print("ocr text is", ocr_text)
    if ratio > threshold:
        return True
    else:
        print("OCR text result of " + str(ocr_text) + "failed threshold for single text")
        if take_failed_screenshot:
            take_failed_screenshot(image)
        return False

def screen_compare_multiple_texts(text_list, threshold=60, take_failed_screenshot=False):
    #Returns False if none of the text matches, otherwise returns the index, original text, and ratio
    image = takescreenshot()
    ocr_text, image = ocr(image)
    ratio_list = [fuzz.partial_ratio(text, ocr_text) for text in text_list]
    if max(ratio_list) < threshold:
        print("OCR text result of " + str(ocr_text) +"failed threshold for multiple text")
        return False
    else:
        return sorted(zip(range(len(ratio_list)), text_list, ratio_list), key=itemgetter(2), reverse=True)[0]

def take_failed_screenshot(image):
    filename = str(time.strftime("%d_%H_%M_%S", time.localtime())) + ".png"
    mouse_pos = pyautogui.position()
    print("Saving ", filename, " as a failure", "\n", "mouse location at ", mouse_pos)
    cv2.imwrite(filename, image)
    full_screen = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    cv2.imwrite("full_" + filename, full_screen)
    rectangle_coords = [mouse_pos[0] - 3, mouse_pos[1] - 3, mouse_pos[0] + 3, mouse_pos[1] + 3]
    rectangle_coords = [max(x, 0) for x in rectangle_coords]
    boxed = cv2.rectangle(full_screen, (rectangle_coords[0], rectangle_coords[1]),
                          (rectangle_coords[2], rectangle_coords[3]),
                          (0, 255, 0), 2)
    cv2.imwrite("boxed_" + filename, boxed)

def print_text_comparisons():
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
        # winsound.Beep(2500, 1000)
    # winsound.Beep(2000, 2000)


def get_txt_from_failed_images():
    image_files = ['16_22_51_19.png',
'16_22_51_21.png',
'16_22_51_22.png']
    for image_file in image_files:
        text = ocr(cv2.imread(image_file), ["thresh"])


if __name__ == '__main__':

    takescreenshot()
