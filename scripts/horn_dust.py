import assets.coordinates as C
from scripts.script_master import B

#Camera 5/5 zoom Eteceteria bank

import random


def humidify(num_seeds):
    locations = C.humidify
    print('initiating...')
    B.print_sleep(3)
    for i in range(int(num_seeds // 27)):
        print('on seed number: ' + str(i * 27))
        # withdraw
        B.easy_move(locations[0])
        B.easy_click()
        B.print_sleep(random.normalvariate(.5, .05))
        B.easy_press('esc')
        # Plant Seeds update
        B.print_sleep(random.normalvariate(.5, .05))
        B.easy_move(locations[1])
        start_spot = locations[1]
        move_spot = locations[2]
        for i in range(25):
            B.easy_click()
            B.print_sleep(random.normalvariate(.5, .05))
            B.easy_move(move_spot)
            B.easy_click()
            B.print_sleep(random.normalvariate(.5, .05))
            start_spot, move_spot = move_spot, start_spot
        # Bank
        B.print_sleep(random.normalvariate(2.0, .2))
        B.easy_move(locations[4])
        B.print_sleep(random.normalvariate(1, .10))
        B.easy_click()
        B.print_sleep(random.normalvariate(1, .1))
        B.easy_move(locations[5])
        B.print_sleep(random.normalvariate(.5, .05))
        B.easy_click()
        B.print_sleep(random.normalvariate(.5, .05))
