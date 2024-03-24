import settings as s

if s.MACHINE == 'ubuntu desktop':
    inventory = [[1702, 807], [1740, 810], [1787, 806], [1823, 808], [1703, 842], [1742, 849], [1787, 845], [1831, 844], [1703, 884], [1741, 880], [1786, 881], [1825, 881], [1699, 917], [1744, 915], [1786, 915], [1828, 910], [1700, 958], [1743, 953], [1782, 952], [1826, 951], [1703, 988], [1743, 983], [1783, 987], [1827, 989], [1701, 1023], [1742, 1025], [1787, 1023], [1827, 1023]]
    inventory_button = [3721, 757]
    screen_pyautogui_region = [1920, 0, 1920, 1080]
    textbox_region = [1924, 920, 516, 160]
    fletch_locations  = [[714, 160], [1776, 915], [1818, 915], [1270, 533], [1019, 841]]
    first_bank_spot = [645, 161]
    prif_furnace = [354, 1007]
    prif_bank_from_furnace =[1412, 263]
    superheat = []

elif s.MACHINE == 't470s':
    inventory = [[1702, 807], [1740, 810], [1787, 806], [1823, 808], [1703, 842], [1742, 849], [1787, 845], [1831, 844], [1703, 884], [1741, 880], [1786, 881], [1825, 881], [1699, 917], [1744, 915], [1786, 915], [1828, 910], [1700, 958], [1743, 953], [1782, 952], [1826, 951], [1703, 988], [1743, 983], [1783, 987], [1827, 989], [1701, 1023], [1742, 1025], [1787, 1023], [1827, 1023]]
    inventory_button = [3721, 757]
    screen_pyautogui_region = [1920, 0, 1920, 1080]
    textbox_region = [1924, 920, 516, 160]
    fletch_locations = [[662, 176], [1744, 913], [1790, 913], [1252, 579], [1017, 857]]
    superheat = [[712, 503], [762, 500], [1684, 902], [1140, 593], [1018, 858], [1018, 858]]