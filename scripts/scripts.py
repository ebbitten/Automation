# requires pyauotgui, pyhook,  pillow,
import pyautogui, time
import math
from game_control import screen_control_bot
from assets import coordinates
from utility.macro import print_sleep
import random
import operating_system.ubuntu_os

pyautogui.FAILSAFE = True

B = screen_control_bot.ScreenBot()


def runNMZAbsorp(laptopType="Desktop", oversConsumed=0, absorpConsumed=0, overConsumeCounter=310, absorpConsumeCounter=600,
                 numOvers=10, numAbsorps=16):
    # TODO load positions from a file
    # TODO initialize should include getting your HP down
    # start timer
    startTime = time.time()
    curTime = time.time()
    lastHeal = time.time()
    # determine the coordinate set we're using
    if laptopType == "Y570":
        invenCoords = [[1195, 256], [1237, 259], [1280, 256], [1155, 288], [1194, 294], [1235, 295], [1279, 292],
                       [1155, 330], [1194, 329], [1238, 331], [1279, 333], [1155, 368], [1198, 368], [1238, 369],
                       [1280, 365], [1155, 405], [1197, 404], [1239, 402], [1278, 403], [1152, 438], [1196, 438],
                       [1235, 442], [1281, 441], [1154, 477], [1194, 477], [1239, 474], [1280, 476]]
        rapidHeal = [1293, 295]
    else:
        invenCoords = [[1700,  808], [1744,  808], [1786,  812], [1826,  812], [1701, 849], [1744, 850], [1785, 851],
                       [1828, 849], [1700, 886], [1742, 883], [1784, 882], [1827, 886], [1700, 921], [1744, 921],
                       [1785, 917], [1827, 919], [1699, 955], [1743, 955], [1785, 958], [1825, 956], [1699, 991],
                       [1742, 990], [1783, 990], [1825, 992], [1702, 1030], [1742, 1028], [1782, 1027], [1832, 1028]]

        rapidHeal = [1835, 843]


    # parse that coordinate let into arrays that we'll use to loop over
    overCoords = invenCoords[:numOvers]
    absorpCoords = invenCoords[numOvers:numAbsorps + numOvers]
    # update consumed counter if we passed any in
    consumedCounter = [overConsumeCounter, absorpConsumeCounter]
    # decrement the amount that we have left based on our consumed counter
    if oversConsumed > 0:
        for i in range(oversConsumed // 4):
            overCoords.pop(0)
    if absorpConsumed > 0:
        for i in range(absorpConsumed // 4):
            absorpCoords.pop(0)
    # update how much time had previously passed based on the consumed counter
    if absorpConsumed > 0 or oversConsumed > 0:
        timeElapsed = max(absorpConsumed * absorpConsumeCounter, oversConsumed * overConsumeCounter)
        startTime = curTime - timeElapsed
    # make our coordinate list that we'll loop over
    coordsList = [overCoords, absorpCoords]
    # initialzie time elapsed
    timeElapsed = curTime - startTime
    # Make the list for how many we'll consider consumed
    consumedList = [oversConsumed, absorpConsumed]
    print("starting in 5")
    B.print_sleep(5)
    while timeElapsed < 30000:
        curTime = time.time()
        timeElapsed = curTime - startTime
        lastHeal = last_heal_time(coordsList, timeElapsed, startTime, consumedList, consumedCounter, lastHeal,
                                  rapidHeal)
        # print(str(consumedList) + "consumed list")
        if not (overCoords or absorpCoords):
            break


def last_heal_time(coords_list, time_elapsed, start_time, consumed_list, consumed_timer, last_heal, rapid_heal):
    time.sleep(1)
    curTime = time.time()
    time_elapsed = curTime - start_time
    print("time elapsed is " + str(time_elapsed))
    # Check if we should drink a prayerpot
    # a prayer dose restores 154 seconds of prayer
    # 0 is over, 1 is pp
    for i in range(2):
        if coords_list[i]:
            B.check_and_consume(i, consumed_timer, coords_list, consumed_list, time_elapsed)
    if time.time() - last_heal > 30:
        B.flick_pray(rapid_heal)
        last_heal = time.time()
    return last_heal


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

def prif_fish(xtime = 4.5 * 60 *60, activity_timer = 125):
    fish_spot = [922, 859]
    time.sleep(2)
    for i in range(math.floor( xtime//(activity_timer+30))):
        B.easy_move(fish_spot)
        print_sleep(random.normalvariate(0.3, 0.05))
        B.easy_click()
        print_sleep(random.normalvariate(activity_timer+10,5))
        drop_inventory(range(0, 26), goto_inven=False)



def tan_dragon_hides(hides, computer="Y570"):
    # TODO fiure out why the 5 mousekey/right clicking doesn't always work
    if computer == "Y570":
        locations = [[677, 139], [1076, 67], [1774, 845], [980, 519], [1751, 783]]
    elif computer == "T470s":
        locations = [[538, 187], [1134, 77], [1781, 723], [989, 506], [1668, 645]]
    else:
        raise ValueError
    phrases = ["Withdraw-1 Green dragonhide", "Close",
               "Cast Tan Leather", "Bank Grand Exchange Booth", "Deposit-1 Green dragon leather"]
    print('initiating...')
    B.print_sleep(5)
    for i in range(int(hides // 25)):
        B.easy_move(locations[0], phrases[0])
        B.easy_right_click()
        B.print_sleep(.2)
        B.easy_mk('num2')
        B.easy_mk('num2')
        B.easy_click()
        B.print_sleep(1)
        B.easy_move(locations[0], phrases[0])
        B.easy_right_click()
        B.print_sleep(.2)
        B.easy_mk('num2')
        B.easy_mk('num2')
        B.easy_click()
        B.print_sleep(1)
        B.easy_move(locations[1], phrases[1])
        B.easy_click()
        B.easy_move(locations[2], phrases[2])
        B.print_sleep(3)
        B.click_wait(6)
        B.easy_move(locations[3], phrases[3])
        B.easy_click()
        B.print_sleep(1.2)
        B.easy_move(locations[4])
        B.easy_right_click()
        B.print_sleep(.2)
        B.easy_mk('num2')
        B.easy_mk('num2')
        B.easy_click()
        B.print_sleep(1)
        B.random_sleep()


def craft_dragon_hides(hides, computer="Y570"):
    # have the needle and thread in inven slots 11 and 12 respectively
    B = screen_control_bot.ScreenBot()
    if computer == "Y570":
        locations = [[677, 139], [1076, 67], [1832, 821], [1794, 820], [980, 519], [1751, 783]]
    elif computer == "T470s":
        locations = [[898, 512], [1136, 78], [1728, 594], [1667, 597], [989, 506], [1667, 648]]
    else:
        raise ValueError
    phrases = ["Withdraw-1 Green dragon leather", "Close",
               "Use Needle", "Use Needle -> Green dragon leather", "Bank Grand Exchange Booth",
               "Deposit-1 Green d'hide body"]
    print('initiating...')
    B.print_sleep(5)
    for i in range(int(hides // 25)):
        B.easy_move(locations[0], phrases[0])
        B.easy_right_click()
        B.print_sleep(.2)
        B.easy_mk("num2")
        B.easy_mk("num2")
        B.easy_click()
        B.print_sleep(1)
        B.easy_click()
        B.easy_move(locations[2], phrases[2])
        B.print_sleep(1.2)
        B.easy_click()
        B.easy_move(locations[3], phrases[3])
        B.easy_click()
        B.print_sleep(1.2)
        B.easy_press("1")
        B.print_sleep(15)
        B.easy_move(locations[4], phrases[4])
        B.easy_move(locations[5])
        B.easy_right_click()
        B.print_sleep(.2)
        B.easy_mk("num2")
        B.easy_mk("num2")
        B.easy_click()
        B.print_sleep(1)


def clean_herbs(num_herbs, computer="desktop", herb_type="torstol"):
    # set withdraw quantity to all
    if computer == "Y570":
        in_game_locations = [[677, 139], [1076, 67], [961, 512], [1031, 825]]
        inventory_locations = [[1752, 751], [1794, 751], [1837, 751], [1878, 748], [1752, 787], [1797, 785],
                               [1837, 785],
                               [1884, 787], [1755, 820], [1797, 820], [1834, 823], [1879, 824], [1757, 856],
                               [1796, 857],
                               [1838, 856], [1883, 859], [1758, 892], [1797, 896], [1838, 892], [1878, 896],
                               [1754, 929],
                               [1798, 932], [1840, 930], [1885, 931], [1756, 966], [1800, 965], [1836, 967],
                               [1886, 968]]
    elif computer == "T470s":
        locations = [[898, 512], [1136, 78], [1728, 594], [1667, 597], [989, 506], [1667, 648]]
    elif computer == 'desktop':
        in_game_locations = [[696, 176], [880, 541]]
        inventory_locations = [[1720, 802], [1761, 798], [1805, 802], [1845, 802], [1722, 836], [1763, 837],
                               [1804, 836],
                               [1846, 838], [1721, 874], [1762, 875], [1803, 874], [1848, 874], [1722, 910],
                               [1763, 907],
                               [1804, 912], [1848, 908], [1722, 946], [1763, 946], [1805, 944], [1847, 947],
                               [1848, 981],
                               [1807, 981], [1764, 980], [1720, 983], [1719, 1016], [1763, 1018], [1803, 1018],
                               [1847, 1018]]
    else:
        raise ValueError
    in_game_phrases = ["Withdraw-1 Grimy " + str(herb_type) + " / 8 more options", "Bank Bank Booth / 3 more options",
                       "Deposit-1 " + str(herb_type)]
    inventory_phrases = ["Clean Grimy " + str(herb_type) + " / 3 more options"]
    already_selected_herb_error_text = "Use " + str(herb_type) + " -> Grimy " + str(herb_type)
    print('initiating...')
    B.print_sleep(5)
    for i in range(int(num_herbs // 28)):
        print('on hides number: ' + str(i * 28))
        # withdraw
        B.easy_move(in_game_locations[0], in_game_phrases[0])
        time.sleep(.3)
        B.easy_click()
        # B.close_screen
        B.print_sleep(1)
        B.easy_press('esc')
        # clean herbs!!
        for inven_loc in [inventory_locations[0]]:
            B.print_sleep(.5)
            passed = False
            ocr_result = B.move_and_decide_text(inven_loc, [inventory_phrases[0], already_selected_herb_error_text],
                                                threshold=60)
            print("OCR result is ", ocr_result)
            if not ocr_result:
                pass
            if ocr_result[1] == inventory_phrases[0]:
                B.print_sleep(.21)
                B.easy_click()
                B.print_sleep(.21)
                print("cleaning")
            elif ocr_result[1] == already_selected_herb_error_text:
                B.click_wait(1)
                print("accidently selected cadantine, clicking")
        time.sleep(33)
        B.random_sleep()

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

def fletch(num_items, action_key='3',activity_timer=45):
    locations = [[714, 160], [1776, 915], [1818, 915], [1270, 533], [1019, 841]]
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


def cook(num_items, action_key='space',activity_timer=59):
    locations = [[711, 160], [1739, 843], [912, 426], [669, 550], [1019, 841]]
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
        B.print_sleep(random.normalvariate(1, .05))
        B.easy_move(locations[2])
        B.easy_click()
        B.print_sleep(random.normalvariate(1.5, .1))
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


def smelt_cannonball(num_steel_bar):
    B.print_sleep(3)
    for i in range(num_steel_bar // 26):
        print(f'on steelbar number {i * 26}')
        B.easy_move(coordinates.first_bank_spot)
        B.print_sleep(random.normalvariate(0.25, 0.2))
        B.easy_click()
        B.easy_move(coordinates.prif_furnace)
        B.print_sleep(random.normalvariate(0.25, 0.2))
        B.easy_click()
        B.print_sleep(random.normalvariate(5, 0.3))
        B.easy_press('space')
        B.print_sleep(random.normalvariate(90, 1))
        B.easy_move(coordinates.prif_bank_from_furnace)
        B.easy_click()
        B.print_sleep(5, 0.3)


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
    # superheat(1390)
    # clean_and_make_potions(587)
    # fletch(411, action_key='')
    # cook(5700, 'space', 59)
    # runNMZAbsorp("Desktop",0, 0, 325, 335, 12, 9)
    drop_inventory(range(0,26))
    prif_fish()
