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





def window_exist(window_name=os.getenv('WINDOW_NAME')):
    screen = Wnck.Screen.get_default()
    if window_name in [window.get_name() for window in screen.get_windows()]:
        return True
    else:
        return False


def start_runelite():
    DETACHED_PROCESS = 8
    if not window_exist("runelite"):
        print('starting waiting')
        runelite = subprocess.Popen(PATH_TO_RUNELITE)
        time.sleep(10)
        print('finished waiting')
    screen = Wnck.Screen.get_default()
    while Gtk.events_pending():
        Gtk.main_iteration()
    windows = screen.get_windows()
    for w in windows:
        print(w.get_name())
        if w.get_name() == 'RuneLite':
            runelite_window = w
    runelite_window.maximize()
    runelite_window.activate(time.time())
    dir(runelite_window)




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
