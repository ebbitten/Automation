import json
import time
import pyautogui
import utility.macro
from operating_system import beep
from pathlib import Path


def get_coord():
    counter = 0
    prevX = 0
    prevY = 0
    while counter < 5:
        time.sleep(.5)
        cur_position = pyautogui.position()
        curX = cur_position[0]
        curY = cur_position[1]
        if curX == prevX and curY == prevY:
            counter += 1
            x = curX
            y = curY
        prevX = curX
        prevY = curY
    beep()
    return [x, y]


def find_coordinates(num_spots, file_path='../assets/mouse_records/scratch.txt'):
    utility.macro.print_sleep(5)
    coords = []
    for i in num_spots:
        new_coord = get_coord()
        coords.append(new_coord)
    beep()
    print(coords)
    with open(Path(file_path),'w+') as f:
        f.writelines(json.dumps(coords))





