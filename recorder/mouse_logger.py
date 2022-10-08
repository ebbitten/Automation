from datetime import datetime
import logging
import time

from pynput.mouse import Listener, Button, Controller
import pandas as pd

logging.basicConfig(filename=f'../data/mouse_training/{datetime.today().strftime("%d_%m_%Y")}.csv',
                    level=logging.DEBUG, format='%(message)s')


def on_move(x, y):
    print(f'{x}, {y}, {time.time()%(60*60*24)}, 0')
    logging.info(f'{x}, {y}, {time.time()%(60*60*24)}, 0')


def on_click(x, y, button, pressed):
    if pressed:
        print(f'{x}, {y}, {time.time()%(60*60*24)}, 1')
        logging.info(f'{x}, {y}, {time.time()%(60*60*24)}, 1')


def on_scroll (x, y, dx, dy):
    print(f'Mouse scrolled at ({x}, {y},) in direction ({dx}, {dy})')

def listen():
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()



if __name__ == '__main__':
    listen()
    time.sleep(5)