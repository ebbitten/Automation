# requires pyauotgui, pyhook,  pillow,
import pyautogui, time
from game_control import screen_control_bot
from assets import coordinates
from game_control.screen_control_bot import print_sleep
import random

pyautogui.FAILSAFE = True

B = screen_control_bot.ScreenBot()


def drop_inventory(xrange=range(0,28), goto_inven=True):
    if goto_inven:
        B.easy_press('esc')
    print_sleep(1)
    with pyautogui.hold('shiftleft'):
        try:
            for inventory_spot in xrange:
                coord = coordinates.inventory[inventory_spot]
                B.easy_move(coord)
                B.easy_click()
            print_sleep(1)
        except:
            pass

def repeat_script(script):
    while True:
        try:
            b = screen_control_bot.ScreenBot()
            b.open_login_deposit()
            script()
        except screen_control_bot.FailedMoveAttempt:
            print('Restarting')
            time.sleep(random.normalvariate(4 * 3600, 1000))

