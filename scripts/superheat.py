from scripts.scripts import B


import random


def superheat(num_seaweed):
    locations = [[759, 486], [809, 485], [795, 544], [1684, 900], [1272, 538], [1021, 844]]
    print('initiating...')
    B.print_sleep(3)
    for i in range(int(num_seaweed // 2)):
        print('on hides number: ' + str(i * 2))
        # withdraw
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