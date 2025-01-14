#!/home/ccpa/bin/firefox/.venv/bin/python

import os, sys
from Xlib import display


def ffuser():
    os.system('ps ax | grep -P Wrightenich > grep.txt') 
    f = open("grep.txt","r")
    greptxt = f.read()
    if f"firefox -P Wrightenich" not in greptxt:
        os.system(f'/usr/bin/firefox -P Wrightenich "https://voice.google.com" &')
    open('grep.txt', 'w').close()

ffuser()

# import gi
# gi.require_version('Wnck', '3.0')
# from gi.repository import Wnck


# def get_winlist():
#     """
#     Get the window list and the active workspace.
#     """
#     scr = Wnck.Screen.get_default()
#     scr.force_update()
#     windows = scr.get_windows()
#     #active_wspace = scr.get_active_workspace()

#     return windows

# wlist = get_winlist()

# for w in wlist:
#     if w.is_active():
#         os.system(f'xseticon -id {w.get_xid()} /home/ccpa/Pictures/conch.png')
#         print(w.get_xid())
#         print(w.get_name())