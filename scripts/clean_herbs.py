from scripts.scripts import B


import time


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