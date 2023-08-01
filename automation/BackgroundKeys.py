import win32gui , win32ui, win32con
import time

class BackgroundKeys:

    WINDOW_NAME =  'USED _getWindowsNames to find the name of the window to where we should sent the key inputs'

    def _getWindowHandler(self):
        hwnd =  win32gui.FindWindow(None , self.WINDOW_NAME)
        return win32ui.CreateWindowFromHandle(hwnd)

    def _getWindowsNames(self):
        def callback(handle, data):
            titles.append(win32gui.GetWindowText(handle))
        titles = []
        win32gui.EnumWindows(callback, None)
        return titles

    def __init__(self):
        self.windowHandler = self._getWindowHandler()


    def _keyConverter(self , key):
        if key =='1':
            return 0x31
        elif key == '2':
            return 0x32
        elif key == '3':
            return 0x33
        elif key == '4':
            return 0x34
        elif key == '5':
            return 0x35
        elif key == '6':
            return 0x36
        elif key == '7':
            return 0x37
        elif key == '8':
            return 0x38
        elif key == '9':
            return 0x39
        elif key == '0':
            return 0x30
        elif key == 'a':
            return 0x41
        elif key == 'b':
            return 0x42
        elif key == 'c':
            return 0x43
        elif key == 'd':
            return 0x44
        elif key == 'e':
            return 0x45
        elif key == 'f':
            return 0x46
        elif key == 'g':
            return 0x47
        elif key == 'h':
            return 0x48
        elif key == 'i':
            return 0x49
        elif key == 'j':
            return 0x4A
        elif key == 'k':
            return 0x4B
        elif key == 'l':
            return 0x4C
        elif key == 'm':
            return 0x4D
        elif key == 'n':
            return 0x4E
        elif key == 'o':
            return 0x4F
        elif key == 'p':
            return 0x50
        elif key == 'q':
            return 0x51
        elif key == 'r':
            return 0x52
        elif key == 's':
            return 0x53
        elif key == 't':
            return 0x54
        elif key == 'u':
            return 0x55
        elif key == 'v':
            return 0x56
        elif key == 'w':
            return 0x57
        elif key == 'x':
            return 0x58
        elif key == 'y':
            return 0x59
        elif key == 'z':
            return 0x5A
        elif key == 'num0':
            return 0x60
        elif key == 'num1':
            return 0x61
        elif key == 'num2':
            return 0x62
        elif key == 'num3':
            return 0x63
        elif key == 'num4':
            return 0x64
        elif key == 'num5':
            return 0x65
        elif key == 'num6':
            return 0x66
        elif key == 'num7':
            return 0x67
        elif key == 'num8':
            return 0x68
        elif key == 'num9':
            return 0x69
        elif key == 'shift':
            return win32con.VK_SHIFT
        elif key == 'control':
            return win32con.VK_CONTROL
        elif key == 'alt':
            return win32con.VK_MENU
        elif key == 'enter':
            return win32con.VK_RETURN
        elif key == 'esc':
            return win32con.VK_ESCAPE

    
    def press(self, key):
        convertedKey = self._keyConverter(key)
        self.windowHandler.SendMessage(win32con.WM_KEYDOWN , convertedKey , 0)
        self.windowHandler.SendMessage(win32con.WM_KEYUP, convertedKey, 0)

    def keyDown(self, key):
        convertedKey = self._keyConverter(key)
        self.windowHandler.SendMessage(win32con.WM_KEYDOWN , convertedKey ,0)

    def keyUp(self, key):
        convertedKey = self._keyConverter(key)
        self.windowHandler.SendMessage(win32con.WM_KEYUP, convertedKey ,0)

    def write(self , string):
        for c in string:
            if str(c).isupper():
                self.keyDown('shift')
                self.press(str(c).lower())
                self.keyUp('shift')
            else:
                self.press(c)

    def pressNTimes(self, key, nTimes):
        count = 0
        while count != nTimes:
            self.press(key)
            count = count +1