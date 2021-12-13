import random
import time


def random_sleep(self, multiplier=1):
    val = random.random()
    if val < multiplier * .01:
        print_sleep(abs(random.normalvariate(40, 5)))
    elif val < multiplier *.05:
        print_sleep(abs(random.normalvariate(7, 3)))
    else:
        print_sleep(abs(random.normalvariate(2,1)))

def print_sleep(time_to_sleep):
    print("time to sleep: ", time_to_sleep)
    time.sleep(time_to_sleep)
