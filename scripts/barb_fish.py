 import time
from game_control.screen_control_bot import print_sleep

from scripts import *
import ocr.ocr_core

FISH_IMAGE_PATH = "/home/adam/PycharmProjects/Automation/assets/images/leaping_sturgeon.png"

FISH_IMAGE_WITH_POLE_PATH ="/home/adam/PycharmProjects/Automation/assets/images/leaping_sturgeon_with_pole.png"
FISH_IMAGE_WITH_POLE_OFFSET = (35, 32)
GLOBAL_OFFSET = (1920, 0)



def main():
    print_sleep(2)
    drop_inventory(range(2,28))
    loc = find_fish()
    print(loc)
    if loc == [-1, -1]:
        return "Couldn't find"
    else:
        B.easy_move(loc)
        B.easy_click()


def find_fish(precision=0.6):
    fish_location = ocr.ocr_core.find_image(FISH_IMAGE_WITH_POLE_PATH, precision)
    if fish_location == [-1, -1]:
        return fish_location
    else:
        return [a+b+c for a,b,c in zip(fish_location, FISH_IMAGE_WITH_POLE_OFFSET, GLOBAL_OFFSET)]

if __name__ == '__main__':
    main()