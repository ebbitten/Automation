from scripts.script_master import B
import assets.coordinates as C

import random


def fletch(num_items, action_key='3',activity_timer=45):
    locations = C.fletch_locations
    print('initiating...')
    B.print_sleep(5)
    for i in range(int(num_items // 27)):
        print('on hides number: ' + str(i * 28))
        # withdraw
        B.easy_move(locations[0])
        B.easy_click()
        # B.close_screen
        B.print_sleep(1)
        B.easy_press('esc')
        # clean herbs!!
        B.easy_move(locations[1])
        B.easy_click()
        B.print_sleep(random.normalvariate(1, .05))
        B.easy_move(locations[2])
        B.easy_click()
        B.print_sleep(random.normalvariate(1.5, .1))
        if action_key:
            B.easy_press(action_key)
        wait_time = 0
        while wait_time < activity_timer:
            wait_time = random.normalvariate(activity_timer + 3, 1)
        B.print_sleep(wait_time)
        B.easy_move(locations[3])
        B.easy_click()
        B.print_sleep(random.normalvariate(1.5, .2))
        B.easy_move(locations[4])
        B.easy_click()
        B.print_sleep(1)