import Xlib
import Xlib.display

def get_all_windows():
    display = Xlib.display.Display()
    root = display.screen().root
    window_ids = root.get_full_property(display.intern_atom('_NET_CLIENT_LIST'), Xlib.X.AnyPropertyType).value
    windows = []
    for window_id in window_ids:
        window = display.create_resource_object('window', window_id)
        windows.append(window)
    return windows

if __name__ == "__main__":
    windows = get_all_windows()
    for window in windows:
        print(window.id)