from scripts.scripts import B, drop_inventory
from game_control.screen_control_bot import print_sleep


import math
import random
import time


def prif_fish(xtime = 4.5 * 60 *60, activity_timer = 125):
    fish_spot = [922, 859]
    time.sleep(2)
    for i in range(math.floor( xtime//(activity_timer+30))):
        B.easy_move(fish_spot)
        print_sleep(random.normalvariate(0.3, 0.05))
        B.easy_click()
        print_sleep(random.normalvariate(activity_timer+10,5))
        drop_inventory(range(0, 26), goto_inven=False)