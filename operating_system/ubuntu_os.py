

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
from gi.repository import Wnck


load_dotenv(find_dotenv())

PATH_TO_RUNELITE = os.getenv('PATH_TO_RUNELITE')



class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)

    def maximize_window(self):
        """Maximizes the window"""
        win32gui.ShowWindow(self._handle, win32con.SW_MAXIMIZE)

    def BringToTop(self):
        win32gui.BringWindowToTop(self._handle)

    def SwitchToWindow(self):
        pass

    def get_activate_window(self):
        self._handle = win32gui.GetForegroundWindow()




def start_runelite():
    DETACHED_PROCESS=8
    # subprocess.Popen(os.system(PATH_TO_RUNELITE))
    os.system(PATH_TO_RUNELITE)
    print('hello')



def window_exist(window_name=os.getenv('WINDOW_NAME')):
    screen = Wnck.Screen.get_default()
    if window_name in [window.get_name() for window in screen.get_windows()]:
        return True
    else:
        return False




def main():
    if not window_exist("runelite"):
        print('starting waiting')
        start_runelite()
        time.sleep(20)
    print('finished waiting')
    # win_mgr.BringToTop()
    # win_mgr.SwitchToWindow()
    # time.sleep(3)
    # win_mgr.maximize_window()

def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst



if __name__ == '__main__':
    main()
    appwindows = get_app_list()
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
