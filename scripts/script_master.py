# requires pyauotgui, pyhook,  pillow,
import pyautogui, time
from assets import coordinates
from game_control import screen_control_bot

from game_control.screen_control_bot import print_sleep
import random
pyautogui.FAILSAFE = True

B = screen_control_bot.ScreenBot()
import scripts


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

if __name__ == '__main__':
    print('hello')
    # scripts.humidify(1000)
    # clean_and_make_potions(1303)
    # fletch(5500, action_key=False, activity_timer=50)
    start_time = time.time()
    print(start_time)
    scripts.cook(7000, 'space', 59)
    end_time = time.time()
    print((end_time))
    print((end_time-start_time)/3600)
    # runNMZAbsorp("Desktop", 0, 0, 310, 397, 16, 8)
    # drop_inventory(range(0,26))
    # prif_fish(105)

