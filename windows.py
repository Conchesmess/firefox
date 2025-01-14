import gi, os
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck
from time import sleep


def get_winlist():
    """
    Get the window list and the active workspace.
    """
    scr = Wnck.Screen.get_default()
    scr.force_update()
    windows = scr.get_windows()
    active_wspace = scr.get_active_workspace()

    return windows, active_wspace

wlist, active_wspace = get_winlist()
print(len(wlist))
for w in wlist:
    if w.is_active():
        #sleep(15)
        xid = w.get_xid()
        os.system(f'xseticon -id {xid} /home/ccpa/Pictures/conch.png')
        print(xid)
        print(w.get_name())
    # if w.is_visible_on_workspace(active_wspace):
    #     print(w.get_name())