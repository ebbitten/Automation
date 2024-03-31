from scripts.script_master import B
import assets.coordinates as C


import random

#up = east full zoom
def cook(num_items, action_key='space',activity_timer=59):
    locations = C.cook
    print('initiating...')
    B.print_sleep(3)
    for i in range(int(num_items // 28)):
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
        B.print_sleep(random.normalvariate(1.5, .1))
        B.easy_press(action_key)
        wait_time = 0
        while wait_time < activity_timer:
            wait_time = random.normalvariate(activity_timer + 3, 1)
        B.print_sleep(wait_time)
        B.easy_move(locations[2])
        B.easy_click()
        B.print_sleep(random.normalvariate(1.5, .2))
        B.easy_move(locations[3])
        B.easy_click()
        B.print_sleep(1)

if __name__ == "__main__":
    cook(28*4, action_key='space',activity_timer=59)