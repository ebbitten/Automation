from dotenv import load_dotenv, find_dotenv
import os
import sys
import subprocess
import multiprocessing as mp
import threading
import time
import re
import psutil
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck, Gtk


load_dotenv(find_dotenv())

PATH_TO_RUNELITE = os.getenv('PATH_TO_RUNELITE')


def window_exist(window_name=os.getenv('WINDOW_NAME')):
    screen = Wnck.Screen.get_default()
    if window_name in [window.get_name() for window in screen.get_windows()]:
        return True
    else:
        return False


def get_runelite_window():
    screen = Wnck.Screen.get_default()
    while Gtk.events_pending():
        Gtk.main_iteration()
    windows = screen.get_windows()
    for w in windows:
        if w.get_name() == 'RuneLite':
            runelite_window = w
    return runelite_window


def activate_window(window):
    window.maximize()
    window.activate(time.time())


def start_runelite():
    DETACHED_PROCESS = 8
    if not window_exist("runelite"):
        print('starting waiting')
        runelite = subprocess.Popen(PATH_TO_RUNELITE)
        time.sleep(10)
        print('finished waiting')
    runelite_window = get_runelite_window()
    activate_window(runelite_window)



if __name__ == '__main__':
    start_runelite()
    # for i in appwindows:
    #     print(i)

    # # SWAPY will record the title and class of the window you want activated
    # app = pywinauto.application.Application()
    # t, c = u'RuneLite.exe', u''
    # print(pywinauto.findwindows.find_windows(title=t))
    # handle = pywinauto.findwindows.find_windows(title=t)[0]
    # # SWAPY will also get the window
    # window = app.window_(handle=handle)
    #
    # # this here is the only line of code you actually write (SWAPY recorded the rest)
    # window.SetFocus()
    # win_mgr = WindowMgr()
    # time.sleep(2)
