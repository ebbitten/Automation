from scripts.script_master import B

from assets.coordinates import coordinates
import random


def superheat(num_seaweed, big_seaweed=False):
    locations = coordinates.superheat
    print('initiating...')
    B.print_sleep(3)
    iter_number = 2 if big_seaweed else 13
    for i in range(int(num_seaweed // iter_number)):
        print('on hides number: ' + str(i * 2))
        # withdraw
        if big_seaweed:
            B.easy_move(locations[0])
            B.easy_click()
            B.print_sleep(random.normalvariate(.5, .05))
            B.easy_click()
            B.easy_move(locations[1])
            B.easy_click()
            B.print_sleep(random.normalvariate(.5, .05))
            B.easy_click()
            B.print_sleep(random.normalvariate(.5, .05))
            B.easy_right_click()
            B.print_sleep(random.normalvariate(.25, .05))
            B.easy_move(locations[2])
            B.print_sleep(random.normalvariate(.5, .05))
            B.easy_click()
        else:
            B.easy_move(locations[0])
            B.easy_click()
            B.print_sleep(random.normalvariate(.5, .05))
            B.easy_move(locations[1])
            B.easy_click()
        # B.close_screen
        B.print_sleep(1)
        B.easy_press('esc')
        # clean herbs!!
        B.easy_move(locations[3])
        B.easy_click()
        B.print_sleep(random.normalvariate(1.5, .05))
        B.easy_move(locations[4])
        B.print_sleep(random.normalvariate(.5, .05))
        B.easy_click()
        B.print_sleep(random.normalvariate(.5, .05))
        B.easy_move(locations[5])
        B.print_sleep(random.normalvariate(.5, .05))
        B.easy_click()
        B.print_sleep(random.normalvariate(.5, .05))