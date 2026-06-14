# encoding=utf-8
from Npp import *
import os
import time
import ctypes

def get_npp_hwnd():
    user32 = ctypes.windll.user32
    hwnd = user32.FindWindowW(u"Notepad++", None)
    if hwnd == 0:
        console.write("Error: Could not find Notepad++ window!\n")
    return hwnd

def update_title_bar(args):
    hwnd = get_npp_hwnd()
    if hwnd == 0:
        return

    # Get current file path (Unicode in Python 2.7)
    file_path = notepad.getCurrentFilename()
    if not isinstance(file_path, unicode):
        file_path = file_path.decode('utf-8')
    file_name = os.path.basename(file_path)

    if os.path.isfile(file_path):
        mod_time = os.path.getmtime(file_path)
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mod_time))
        new_title = u"{} - {} - Notepad++".format(file_name, time_str)
    else:
        new_title = u"{} - Unsaved - Notepad++".format(file_name)

    user32 = ctypes.windll.user32
    user32.SetWindowTextW(hwnd, new_title)

# Register callback only once
try:
    i_am_installed
except NameError:
    notepad.callback(update_title_bar,
                     [NOTIFICATION.BUFFERACTIVATED, NOTIFICATION.FILESAVED])
    i_am_installed = True
    console.write("Title bar update script is now active (Unicode safe)!\n")
else:
    console.write("Title bar update script is already running.\n")

# --- Immediately update the title bar for the current file ---
update_title_bar(None)