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

TEXTBOXY580_E = (0, 31, 300, 25)

def takescreenshot():
    image = pyautogui.screenshot(region=TEXTBOXY580_E)
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
    # cv2.imwrite("gray_screenshot.png", gray)
    text = pytesseract.image_to_string(Image.open("gray_screenshot.png"))
    print(text)
    # cv2.imshow("Image", image)
    # cv2.imshow("Output", gray)
    # cv2.waitKey(0)
    return text, gray

def screen_and_compare(text, threshold=80):
    image = takescreenshot()
    ocr_text, image = ocr(image)
    ratio = fuzz.partial_ratio(text, ocr_text)
    print("ratio is ", ratio)
    print("original text was ", text)
    print("ocr text is", ocr_text)
    if ratio > threshold:
        return True
    else:
        filename = "ocr_" + str(ocr_text) + "_exp_" + str(text) + str(time.strftime("%d_%H_%M_%S", time.localtime())) + ".png"
        print("Saving ", filename, " as a failure")
        cv2.imwrite(filename, image)
        full_screen = pyautogui.screenshot()
        cv2.imwrite("full_" + filename, cv2.cvtColor(np.array(full_screen), cv2.COLOR_RGB2BGR))


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


def test_failed():
    image_files = ['failed_screenshot 1537068659.2704172.png',
'failed_screenshot 1537068821.6277032.png',
'failed_screenshot 1537068992.083453.png',
'failed_screenshot 1537068993.2545197.png',
'failed_screenshot 1537069018.849984.png',
'failed_screenshot 1537069020.0530527.png',
'failed_screenshot 1537069021.2351203.png',
'failed_screenshot 1537069104.0978599.png',
'failed_screenshot 1537069200.5273755.png',
'failed_screenshot 1537069201.7184436.png',
'failed_screenshot 1537069202.8805096.png',
'failed_screenshot 1537069252.0853243.png',
'failed_screenshot 1537069273.5775535.png',
'failed_screenshot 1537069336.7071645.png',
'failed_screenshot 1537069337.800227.png',
'failed_screenshot 1537069365.4518085.png',
'failed_screenshot 1537069366.6408763.png',
'failed_screenshot 1537069435.4698133.png',
'failed_screenshot 1537069436.6908832.png',
'failed_screenshot 1537069437.86195.png',
'failed_screenshot 1537069495.856267.png',
'failed_screenshot 1537069505.6358263.png',
'failed_screenshot 1537069541.1758592.png',
'failed_screenshot 1537069548.112256.png',
'failed_screenshot 1537069551.7324631.png',
'failed_screenshot 1537069589.1186016.png',
'failed_screenshot 1537069596.0469978.png',
'failed_screenshot 1537069599.5892005.png',
'failed_screenshot 1537069614.9980814.png',
'failed_screenshot 1537069616.2361524.png',
'failed_screenshot 1537069617.41822.png',
'failed_screenshot 1537069627.6668062.png',
'failed_screenshot 1537069634.604203.png',
'failed_screenshot 1537069638.2264102.png',
'failed_screenshot 1537069653.643292.png',
'failed_screenshot 1537069664.2378979.png',
'failed_screenshot 1537069671.2062967.png',
'failed_screenshot 1537069674.724498.png',
'failed_screenshot 1537069690.0563748.png',
'failed_screenshot 1537069691.217441.png',
'failed_screenshot 1537069692.368507.png',
'failed_screenshot 1537069702.4460833.png',
'failed_screenshot 1537069709.786503.png',
'failed_screenshot 1537069713.4647138.png',
'failed_screenshot 1537069729.069606.png',
'failed_screenshot 1537069745.6785562.png',
'failed_screenshot 1537069749.2837622.png',
'failed_screenshot 1537069765.0226624.png',
'failed_screenshot 1537069766.2517328.png',
'failed_screenshot 1537069767.4007988.png',
'failed_screenshot 1537069777.341367.png',
'failed_screenshot 1537069784.404771.png',
'failed_screenshot 1537069785.2528198.png',
'failed_screenshot 1537069786.0668662.png',
'failed_screenshot 1537069789.2000453.png',
'failed_screenshot 1537069813.9534612.png',
'failed_screenshot 1537069814.7595072.png',
'failed_screenshot 1537069815.5755541.png',
'failed_screenshot 1537069821.7789087.png',
'failed_screenshot 1537069825.1961043.png',
'failed_screenshot 1537069840.4999795.png',
'failed_screenshot 1537069851.4286046.png',
'failed_screenshot 1537069858.4770079.png',
'failed_screenshot 1537069862.117216.png',
'failed_screenshot 1537069877.3070848.png',
'failed_screenshot 1537069888.2137089.png',
'failed_screenshot 1537069895.1081028.png',
'failed_screenshot 1537069898.6173038.png',
'failed_screenshot 1537069931.442181.png',
'failed_screenshot 1537069938.1955676.png',
'failed_screenshot 1537069941.6547654.png',
'failed_screenshot 1537069979.901953.png',
'failed_screenshot 1537069981.1660252.png',
'failed_screenshot 1537069982.3540933.png',
'failed_screenshot 1537069988.7974617.png',
'failed_screenshot 1537070002.1422248.png',
'failed_screenshot 1537070017.8351226.png',
'failed_screenshot 1537070019.0601928.png',
'failed_screenshot 1537070020.2342596.png',
'failed_screenshot 1537070030.20083.png',
'failed_screenshot 1537070037.109225.png',
'failed_screenshot 1537070040.674429.png',
'failed_screenshot 1537070134.2947838.png',
'failed_screenshot 1537070135.5038528.png',
'failed_screenshot 1537070136.7079217.png']
    for image_file in image_files:
        text = ocr(cv2.imread(image_file), ["thresh"])


