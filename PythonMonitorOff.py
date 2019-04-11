import sys
import time
if sys.platform.startswith("linux"):
    import os
    os.system('xset dpms force off')
elif sys.platform.startswith('win'):
    import win32con,win32gui
    from os import getpid,system
    def poweroff():
        abc=0xF170
        win32gui.SendMessage(win32con.HWND_BROADCAST,win32con.WM_SYSCOMMAND,abc,2)
    def poweron():
        abc=0xF170
        win32gui.SendMessage((win32con.HWND_BROADCAST,win32con.WM_SYSCOMMAND,abc,-1))
    if __name__=='__main__':
        poweroff()
        time.sleep(1)
        poweron()
