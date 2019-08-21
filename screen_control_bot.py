import random
import time
import winsound
import pyautogui
import ocr


class ScreenBot():
    def __init__(self):
        self.cur_pos = []
        self.prev_pos = []
        self.cur_fails = 0
        self.total_fails = 0
        self.time_active = 0
        self.time_sleeping = 0

    def click_wait(self, num):
        for i in range(num):
            self.easy_click()
            self.print_sleep(abs(random.normalvariate(1.4, .1)))
            self.random_sleep()

    def random_sleep(self):
        if random.random() < .01:
            self.print_sleep(abs(random.normalvariate(40, 5)))
        if random.random() < .05:
            self.print_sleep(abs(random.normalvariate(7, 3)))
        if random.random() < .002:
            print('browsing')
            # helperLoop.randomBrowsing()
            print('browsing not currently implemented')
            # TODO re-implement but make sure it ends up back in the same spot

    def easy_move(self, location, text="", take_failed_screenshot=False, threshold=80, max_attempts=3):
        self.human_move(location[0], location[1], 1.2, 8)
        time.sleep(.2)
        global FAILED_MOVE_ATTEMPTS
        global MAX_FAILED_MOVE_ATTEMPTS
        if text:
            attempts = 0
            while attempts < max_attempts:
                if ocr.screen_and_compare(text, threshold, take_failed_screenshot):
                    return True
                else:
                    self.human_move(location[0], location[1], .3, 1, jiggle=True)
                    self.print_sleep(.5)
                    attempts += 1
            if attempts == max_attempts:
                FAILED_MOVE_ATTEMPTS += 1
                print(FAILED_MOVE_ATTEMPTS)
            if FAILED_MOVE_ATTEMPTS >= MAX_FAILED_MOVE_ATTEMPTS:
                raise FailedMoveAttempt('too many failed movements')




    def human_move(self, finalx, finaly, totalTime, steps, jiggle=False):
        tweens = [pyautogui.easeOutQuad, pyautogui.easeInQuad, pyautogui.easeInOutQuad]
        starting_pos = pyautogui.position()
        # If we're already on the spot just go ahead and get ready to click
        if not jiggle:
            if ((abs(finalx - starting_pos[0]) + abs(finaly - starting_pos[1])) ** .5) < 5:
                return
        # otherwise move there over a series of steps
        # TODO make this look a lot more "human"
        step_variance = 5
        last_variance = 3
        if jiggle:
            last_variance = 5
        for i in range(1, steps + 1):
            tween_choice = random.choice(tweens)
            x = starting_pos[0] * (steps - i) / steps + finalx * (i) / steps
            y = starting_pos[1] * (steps - i) / steps + finaly * (i) / steps
            if i < steps:
                x += random.normalvariate(0, step_variance)
                y += random.normalvariate(0, step_variance)
            elif i == steps:
                x += random.normalvariate(0, last_variance)
                y += random.normalvariate(0, last_variance)
            stepTime = totalTime / steps
            pyautogui.moveTo(x, y, stepTime, tween_choice, None, False)

    def easy_press(self, key):
        pyautogui.press(key, interval=(random.normalvariate(25, 5) / 100))

    def easy_click(self):
        self.do_click(clicks=1, duration=(random.normalvariate(25, 3) / 100))

    def easy_right_click(self):
        self.do_click(clicks=1, button='right', duration=(random.normalvariate(35, 3) / 100))

    def do_click(self, clicks=1, interval=0.0, button='left', duration=0.0):
        try:
            pyautogui.click(clicks=clicks, interval=interval, button=button, duration=duration)
        except:
            try:
                pyautogui.click(clicks=clicks, interval=interval, button=button, duration=duration)
            except:
                pass

    def print_sleep(self, time_to_sleep):
        if time_to_sleep > 2:
            print("time to sleep: ", time_to_sleep)
        time.sleep(time_to_sleep)

    def get_coord(self):
        counter = 0
        prevX = 0
        prevY = 0
        while counter < 5:
            self.print_sleep(.5)
            curposition = pyautogui.position()
            curX = curposition[0]
            curY = curposition[1]
            if curX == prevX and curY == prevY:
                counter += 1
                x = curX
                y = curY
            prevX = curX
            prevY = curY
        winsound.Beep(2500, 1000)
        return [x, y]

    def find_coordinates(self, hw, over_loads, prayer_pots):
        # assume that the first position is holy wrench
        # the second through 8th position are overloads
        # the 9th through 28th position are prayer pots
        hw_coords = []
        over_coords = []
        pp_cords = []
        self.print_sleep(5)
        for i in range(hw):
            new_coord = self.get_coord()
            hw_coords.append(new_coord)
        for i in range(over_loads):
            new_coord = self.get_coord()
            over_coords.append(new_coord)
        for i in range(prayer_pots):
            new_coord = self.get_coord()
            pp_cords.append(new_coord)
        winsound.Beep(2000, 2000)
        print(hw_coords)
        print(over_coords)
        print(pp_cords)
        filePath = input("please input a filepath to save the coordinates")





class FailedMoveAttempt(Exception):
    "Raised when there's too many failed movement attempts"
    pass