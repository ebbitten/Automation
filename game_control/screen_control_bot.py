import utility.macro
from operating_system.ubuntu_os import start_runelite
from recorder.mouse_over import get_coord
from utility.macro import print_sleep
import pyautogui
import torch
import numpy
from natural_mouse_movements import init_model
import game_control.mouse_control.bezmouse
from pathlib import Path
from ocr import ocr_core
import os
import random
import time
import math


pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True
MAX_FAILED_MOVE_ATTEMPTS = 15
FAILED_MOVE_ATTEMPTS = 0
FAILED_MOVE_ATTEMPTS = 0
MAX_FAILED_MOVE_ATTEMPTS = 0
TIME_MODEL_PATH = Path("/home/adam/PycharmProjects/Automation/natural_mouse_movements/models/time/time-state-dict.pth")
PATH_MODEL_PATH = Path("/home/adam/PycharmProjects/Automation/natural_mouse_movements/models/path/path-state-dict.pth")



# T470s with screen
# COORDS ={ 'Click Here To Play': [937, 491],
#           'Bank': [950, 499],
#           'bank_tab_1': [559, 116],
#           'Deposit inventory': [1042, 733]
#
#
# }
# BOXES = {
# 'Welcome to Runescape': (800, 381, 252, 39)
# }

# Y580

COORDS ={ 'Click Here To Play': [970, 368],
          'Bank': [960, 521],
          'bank_tab_1': [709, 127],
          'Deposit inventory': [1032, 846]


}
BOXES = {
}


class ScreenBot():
    def __init__(self, max_cur_failed_attempts=2, max_total_failed_attempts=100, text_compare_threshold=70,
                 take_failed_screen=False, take_success_screen=False):
        self.cur_pos = []
        self.prev_pos = []
        self.cur_fails = 0
        self.total_fails = 0
        self.time_active = 0
        self.time_sleeping = 0
        self.max_cur_failed_attempts = max_cur_failed_attempts
        self.max_total_failed_attempts = max_total_failed_attempts
        self.text_compare_threshold = text_compare_threshold
        self.take_failed_screen = take_failed_screen
        self.take_success_screen = take_success_screen
        self.is_moving = False
        self.time_model = init_model.TimeNet()
        self.time_model.load_state_dict(torch.load(TIME_MODEL_PATH))
        self.time_model.eval()
        self.path_model = init_model.PathNet()
        self.path_model.load_state_dict(torch.load(PATH_MODEL_PATH))
        self.path_model.eval()
        self.print_sleep = utility.macro.print_sleep
        self.random_sleep = utility.macro.random_sleep

    def click_wait(self, num):
        for i in range(num):
            self.easy_click()
            print_sleep(abs(random.normalvariate(1.4, .1)))
            utility.macro.random_sleep()

    def random_browsing(self):
        final_x, final_y = get_coord()
        print("Random Browsing")
        screenWidth, screenHeight = pyautogui.size()
        for i in range(int(max(random.normalvariate(5, 1),1))):
            x = random.randint(1, screenWidth)
            y = random.randint(1, screenHeight)
            self.easy_move((x, y),tolerance=10)
            time.sleep(abs(random.normalvariate(1, .2)))
        self.easy_move((final_x, final_y))

    def retry_move(self, location_0, location_1):
        self.cur_fails += 1
        self.total_fails += 1
        print_sleep(.5)
        if self.total_fails == self.max_total_failed_attempts:
            raise FailedMoveAttempt('too many failed movements')
        elif self.cur_fails == self.max_cur_failed_attempts:
            print("Self total fails: " + str(self.total_fails))
            print_sleep(2)
            self.random_browsing()
        else:
            self._human_move_bez((location_0, location_1))

    def easy_move(self, location, text="", tolerance=4, deviation=4):
        # while math.dist(pyautogui.position(), location)>tolerance:
        #     self._human_move_bez(location[0], location[1], deviation)
        self._human_move_bez(location[0], location[1], deviation+4)
        self._human_move_bez(location[0], location[1], deviation)
        self.is_moving = True
        self.cur_fails = 0
        if text:
            while self.is_moving:
                time.sleep(.3)
                if ocr_core.screen_and_compare(text, self.text_compare_threshold, self.take_failed_screen):
                    self.is_moving = False
                    return True
                else:
                    self.retry_move(location[0], location[1])

    def move_and_decide_text(self, location, text_list, threshold=80, max_attempts=3):
        self.easy_move((location[0], location[1]))
        print_sleep(.2)
        self.cur_fails = 0
        self.is_moving = True
        while self.is_moving:
            top_text_result = ocr_core.screen_compare_multiple_texts(text_list, threshold)
            if top_text_result:
                self.is_moving = False
                return top_text_result
            else:
                self.retry_move(location[0], location[1])


    def _human_move_ml(self, finalx, finaly, totalTime, steps, jiggle=False):
        self.prev_pos = self.cur_pos
        starting_pos = pyautogui.position()
        screen_size = pyautogui.size()
        values = ((finalx - starting_pos[0])/screen_size[0],
                  (finaly - starting_pos[1])/screen_size[1])
        numpy_values = numpy.array(values).reshape(1,2)
        inputs = torch.Tensor(numpy_values)
        print(inputs)
        times = self.time_model(inputs).reshape(100)
        paths = self.path_model(inputs)
        for time, path in zip(times, paths):
            # print(float(path[0]))
            # print(float(path[1]))
            # print(float(time))
            # print(float(path[0])*screen_size[0], float(path[1])*screen_size[1], float(time))
            pyautogui.moveTo(float(path[0])*screen_size[0], float(path[1])*screen_size[1], float(time))
        print(f'expected to go to {finalx}, {finaly}')
        print(f'actually went to {pyautogui.position()[0]}, {pyautogui.position()[1]}')

    def _human_move_bez(self, finalx, finaly, deviation=6):
        game_control.mouse_control.bezmouse.move_to_area(finalx, finaly, 4, 5, deviation, 5)



    def easy_press(self, key):
        pyautogui.press(key, interval=(random.normalvariate(25, 5) / 100))

    def easy_presses(self, keys):
        for key in keys:
            self.easy_press(key)

    def easy_mk(self, numkey):
        dist = 32
        if numkey == 'num2':
            pyautogui.moveRel(0,35,.5).main()

    def easy_click(self):
        self._do_click(clicks=1, duration=(random.normalvariate(25, 3) / 100))

    def easy_right_click(self):
        self._do_click(clicks=1, button='right', duration=(random.normalvariate(35, 3) / 100))

    def _do_click(self, clicks=1, interval=0.0, button='left', duration=0.0):
        print("click")
        try:
            pyautogui.click(clicks=clicks, interval=interval, button=button, duration=duration)
        except:
            try:
                print('click failed')
                pyautogui.click(clicks=clicks, interval=interval, button=button, duration=duration)
            except:
                pass

    def flick_pray(self, rapidHeal):
        randInterval = random.randint(20, 30) / 100
        pyautogui.press('f5', interval=randInterval)
        time.sleep(random.randint(25, 35) / 100)
        randInterval = random.normalvariate(25, 3) / 10
        self.easy_move((rapidHeal[0], rapidHeal[1]))
        self._do_click(clicks=1, duration=(random.normalvariate(25, 3) / 100))
        time.sleep(random.randint(150, 200) / 100)
        self._do_click(clicks=1, duration=(random.normalvariate(25, 3) / 100))
        time.sleep(random.normalvariate(175, 15) / 100)
        randInterval = random.normalvariate(25, 3) / 100
        pyautogui.press('esc', interval=randInterval)


    def check_and_consume(self, consumed_type, consumed_timer, coords_list, consumed_list, time_elapsed):
        if time_elapsed - consumed_timer[consumed_type] * consumed_list[consumed_type] > consumed_timer[consumed_type]:
            typename = ["Overload", "Prayer Potion"]
            print(("Drinking " + str(typename[consumed_type]) + "\n") * 3)
            time.sleep(2)
            # move to our potion
            x = coords_list[consumed_type][0][0] + random.normalvariate(0, 2)
            y = coords_list[consumed_type][0][1] + random.normalvariate(0, 2)
            moveTime = random.randrange(20, 40, 1) / 10
            self.easy_move((x, y))
            # click
            time.sleep(.25)
            self._do_click(duration=random.normalvariate(20, 3) / 100)
            time.sleep(.5)
            # Move to a random location occasionly
            # update our consumption
            consumed_list[consumed_type] += 1
            if consumed_list[consumed_type] % 4 == 0:
                coords_list[consumed_type].pop(0)
            if typename[consumed_type] == "Overload" and len(coords_list[consumed_type]) == 1 and consumed_list[
                consumed_type] % 4 == 3:
                coords_list[consumed_type].pop(0)
                consumed_list[consumed_type] += 1
            if random.randint(0, 20) > 18:
                self.random_browsing()

    def click_on_bank(self):
        self.easy_move(COORDS['Bank'])
        self.easy_click()
        pass

    def click_on_bank_tab(self, tab=1):
        tab_coord = COORDS['bank_tab_'+str(tab)]
        self.easy_move(tab_coord)
        self.easy_click()

    def click_deposit_inventory(self):
        self.easy_move(COORDS['Deposit inventory'])
        self.easy_click()

    def login(self):
        if not ocr.ocr_lib.imagesearch('/home/adam/PycharmProjects/Automation/assets/images/Welcome to Runescape.png', .7):
            self.easy_press('enter')
            print('Disconnected, adding an extra enter click')
        self.easy_press('enter')
        keys = [str(x) for x in os.getenv('PASSWORD')]
        self.easy_presses(keys)
        self.easy_press('enter')
        time.sleep(5)
        self.easy_move(COORDS['Click Here To Play'])
        self.easy_click()
        time.sleep(5)
        pyautogui.keyDown('down')
        time.sleep(random.normalvariate(2.2, .2))
        pyautogui.keyUp('down')

    def open_and_login(self):
        start_runelite()
        self.login()


    def open_login_deposit(self):
        self.open_and_login()
        time.sleep(1)
        self.click_on_bank()
        time.sleep(1)
        self.click_on_bank_tab(tab=1)
        time.sleep(1)
        self.click_deposit_inventory()

    


class FailedMoveAttempt(Exception):
    "Raised when there's too many failed movement attempts"
    pass


if __name__ == '__main__':
    # pass
    b = ScreenBot()
    # b.open_login_deposit()

