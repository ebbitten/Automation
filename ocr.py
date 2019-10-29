from PIL import Image
import pytesseract
import argparse
import imutils
import time
from fuzzywuzzy import fuzz
import winsound
import math
from operator import itemgetter
import pyautogui
import random
import time
import platform
import subprocess
import cv2
import numpy as np
import pyautogui
import time
import platform
import subprocess

is_retina = False
if platform.system() == "Darwin":
    is_retina = subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True)

#TODO move into a config file
#t470s
#tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata\\configs"'
#tesseract_cmd = 'C:\\Users\\Adam\\Downloads\\jTessBoxEditor-2.0.1\\jTessBoxEditor\\tesseract-ocrtesseract\\tesseract'
TESSDATA_PREFIX=r"C:\Program Files\Tesseract-OCR\tessdata"


#y580
tesseract_cmd = 'C:\\Program Files \\Tesseract-OCR\\tesseract'

TEXTBOXY580_E = (0, 31, 300, 25)

'''
grabs a region (topx, topy, bottomx, bottomy)
to the tuple (topx, topy, width, height)
input : a tuple containing the 4 coordinates of the region to capture
output : a PIL image of the area selected.
'''


def region_grabber(region):
    x1 = region[0]
    y1 = region[1]
    width = region[2] - x1
    height = region[3] - y1

    return pyautogui.screenshot(region=(x1, y1, width, height))


'''
Searchs for an image within an area
input :
image : path to the image file (see opencv imread for supported types)
x1 : top left x value
y1 : top left y value
x2 : bottom right x value
y2 : bottom right y value
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
im : a PIL image, usefull if you intend to search the same unchanging region for several elements
returns :
the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not
'''


def imagesearcharea(image, x1, y1, x2, y2, precision=0.8, im=None):
    if im is None:
        im = region_grabber(region=(x1, y1, x2, y2))
        # im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc


'''
Searchs for an image on the screen
input :
image : path to the image file (see opencv imread for supported types)
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
im : a PIL image, usefull if you intend to search the same unchanging region for several elements
returns :
the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not
'''


def imagesearch(image, precision=0.8):
    im = pyautogui.screenshot()
    if is_retina:
        im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
    # im.save('testarea.png') useful for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]
    # recognizer = cv2.face.LBPHFaceRecognizer_create()
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc


'''
Searchs for an image on screen continuously until it's found.
input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image 
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
returns :
the top left corner coordinates of the element if found as an array [x,y] 
'''


def imagesearch_loop(image, timesample, precision=0.8):
    pos = imagesearch(image, precision)
    while pos[0] == -1:
        print(image + " not found, waiting")
        time.sleep(timesample)
        pos = imagesearch(image, precision)
    return pos


'''
Searchs for an image on screen continuously until it's found or max number of samples reached.
input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image
maxSamples: maximum number of samples before function times out.
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
returns :
the top left corner coordinates of the element if found as an array [x,y] 
'''


def imagesearch_numLoop(image, timesample, maxSamples, precision=0.8):
    pos = imagesearch(image, precision)
    count = 0
    while pos[0] == -1:
        print(image + " not found, waiting")
        time.sleep(timesample)
        pos = imagesearch(image, precision)
        count = count + 1
        if count > maxSamples:
            break
    return pos


'''
Searchs for an image on a region of the screen continuously until it's found.
input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image 
x1 : top left x value
y1 : top left y value
x2 : bottom right x value
y2 : bottom right y value
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
returns :
the top left corner coordinates of the element as an array [x,y] 
'''


def imagesearch_region_loop(image, timesample, x1, y1, x2, y2, precision=0.8):
    pos = imagesearcharea(image, x1, y1, x2, y2, precision)

    while pos[0] == -1:
        time.sleep(timesample)
        pos = imagesearcharea(image, x1, y1, x2, y2, precision)
    return pos


'''
Searches for an image on the screen and counts the number of occurrences.
input :
image : path to the target image file (see opencv imread for supported types)
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.9
returns :
the number of times a given image appears on the screen.
optionally an output image with all the occurances boxed with a red outline.
'''


def imagesearch_count(image, precision=0.9):
    img_rgb = pyautogui.screenshot()
    if is_retina:
        img_rgb.thumbnail((round(img_rgb.size[0] * 0.5), round(img_rgb.size[1] * 0.5)))
    img_rgb = np.array(img_rgb)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= precision)
    count = 0
    for pt in zip(*loc[::-1]):  # Swap columns and rows
        # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2) // Uncomment to draw boxes around found occurances
        count = count + 1
    # cv2.imwrite('result.png', img_rgb) // Uncomment to write output image with boxes drawn around occurances
    return count






def takescreenshot(region=TEXTBOXY580_E):
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
        winsound.Beep(2500, 1000)
    winsound.Beep(2000, 2000)


def get_txt_from_failed_images():
    image_files = ['16_22_51_19.png',
'16_22_51_21.png',
'16_22_51_22.png']
    for image_file in image_files:
        text = ocr(cv2.imread(image_file), ["thresh"])


if __name__ == '__main__':

    print(loc)
    b.easy_move(loc)
