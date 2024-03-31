from scripts.script_master import B


import random
import time


def clean_and_make_potions(num_herbs):
    locations = [[710, 160], [755, 162], [1736, 915], [1778, 915], [1270, 533], [805, 158], [1019, 841]]
    print('initiating...')
    B.print_sleep(5)
    for i in range(int(num_herbs // 14)):
        print('on hides number: ' + str(i * 14))
        # withdraw
        B.easy_move(locations[0])
        B.easy_click()
        time.sleep(random.normalvariate(.3,.05))
        B.easy_move(locations[1])
        B.easy_click()
        # B.close_screen
        B.print_sleep(1)
        B.easy_press('esc')
        # clean herbs!!
        B.easy_move(locations[2])
        B.easy_click()
        wait_time = 0
        while wait_time < 18:
            wait_time = random.normalvariate(21,1)
        B.print_sleep(wait_time)
        B.easy_click()
        B.easy_move(locations[3])
        B.print_sleep(random.normalvariate(.5, .05))
        B.easy_click()
        B.print_sleep(random.normalvariate(1.5, .1))
        B.easy_press('space')
        wait_time = 0
        while wait_time < 9:
            wait_time = random.normalvariate(12,1)
        B.print_sleep(wait_time)
        B.easy_move(locations[4])
        B.easy_click()
        B.print_sleep(random.normalvariate(1.5, .2))
        B.easy_move(locations[5])
        B.easy_click()
        B.print_sleep(random.normalvariate(1, .1))
        B.easy_press('esc')
        B.easy_move(locations[2])
        B.easy_click()
        B.print_sleep(random.normalvariate(1, .1))
        B.easy_move(locations[3])
        B.easy_click()
        B.print_sleep(random.normalvariate(1.5, .1))
        B.easy_press('space')
        wait_time = 0
        while wait_time < 15:
            wait_time = random.normalvariate(15, 1)
        B.print_sleep(wait_time)
        B.easy_move(locations[4])
        B.easy_click()
        B.print_sleep(random.normalvariate(1, .1))
        B.easy_move(locations[6])
        B.easy_click()
        B.print_sleep(1)