
import logging
import time

from pynput.mouse import Listener, Button, Controller
import pandas as pd

def on_move(x, y):
    print(f'Mouse moved to ({x}, {y}) at t={time.time()}')

def on_click(x, y, button, pressed):
    if pressed:
        print(f'Mouse clicked at ({x}, {y}) with {button}at t={time.time()}')

def on_scroll (x, y, dx, dy):
    print(f'Mouse scrolled at ({x}, {y},) in direction ({dx}, {dy})')

def listen():
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()



if __name__ == '__main__':
    listen()
    time.sleep(5)
