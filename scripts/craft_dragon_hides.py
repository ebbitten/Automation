from game_control import screen_control_bot


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