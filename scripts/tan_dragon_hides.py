from scripts.scripts import B


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