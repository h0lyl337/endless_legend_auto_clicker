import win32api, win32con
import win32com
import win32gui
import time
import psutil
import subprocess
import threading

proc_list = []
handle = int()
is_bot = True


#ENDLESSCWORLD BOTS BOT V1.0

def click():
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)

def keyboard():
    win32api.keybd_event(win32con.VK_LEFT, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    win32api.keybd_event(win32con.VK_LEFT, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)


def startclickbot(handle):
    click()
    keyboard()


def open_chest():
    x1 = int(41)
    y1 = int(198)
    win32api.SetCursorPos((x1, y1))
    win32api.SendMessage(handle, win32con.WM_MBUTTONDOWN, win32con.MOUSEEVENTF_LEFTDOWN)
    win32api.SendMessage(handle, win32con.WM_MBUTTONUP, win32con.MOUSEEVENTF_LEFTUP)


def auto_fuse():
    global is_bot
    is_bot = False
    print('auto fusing')


    x1 = int(227)
    y1 = int(635)
    x2 = int(992)
    y2 = int(629)
    x3 = int(719)
    y3 = int(416)

    win32gui.SetForegroundWindow(handle)
    win32api.SetCursorPos((x1,y1))
    win32api.SendMessage(handle, win32con.WM_MBUTTONDOWN, win32con.MOUSEEVENTF_LEFTDOWN)
    win32api.SendMessage(handle, win32con.WM_MBUTTONUP, win32con.MOUSEEVENTF_LEFTUP)

    time.sleep(1)

    win32api.SetCursorPos((x2, y2))
    win32api.SendMessage(handle, win32con.WM_MBUTTONDOWN, win32con.MOUSEEVENTF_LEFTDOWN)
    win32api.SendMessage(handle, win32con.WM_MBUTTONUP, win32con.MOUSEEVENTF_LEFTUP)

    time.sleep(1)

    win32api.SetCursorPos((x3, y3))
    win32api.SendMessage(handle, win32con.WM_MBUTTONDOWN, win32con.MOUSEEVENTF_LEFTDOWN)
    win32api.SendMessage(handle, win32con.WM_MBUTTONUP, win32con.MOUSEEVENTF_LEFTUP)

    win32api.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_ESCAPE)
    win32api.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_ESCAPE)

    is_bot = True

def is_running():
    for proc in psutil.process_iter():
        proc_list.append(proc.name())
    if 'EndlessWorld.exe' in proc_list:
        print('game was found running already!')
        print('go to game window within 5 seconds')
        time.sleep(6)
        game_handle = win32gui.GetForegroundWindow()
        global handle
        handle = game_handle
        win32gui.ShowWindow(game_handle, 3)
        print(game_handle)
        time.sleep(10)
        win32api.SetCursorPos((509, 343))
        win32api.SendMessage(game_handle, win32con.WM_MBUTTONDOWN, win32con.MOUSEEVENTF_LEFTDOWN)
        win32api.SendMessage(game_handle, win32con.WM_MBUTTONUP, win32con.MOUSEEVENTF_LEFTUP)

    elif 'EndlessWorld.exe' not in proc_list:
        print('Game not running, attempting to start now.')
        subprocess.call('C:\Program Files (x86)\Steam\steam.exe -applaunch 840260')
        time.sleep(3)
        print(win32gui.GetForegroundWindow())
        game_handle = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(game_handle, 3)

        time.sleep(10)

        win32api.SetCursorPos((509, 343))
        win32api.SendMessage(game_handle, win32con.WM_MBUTTONDOWN, win32con.MOUSEEVENTF_LEFTDOWN)
        win32api.SendMessage(game_handle, win32con.WM_MBUTTONUP, win32con.MOUSEEVENTF_LEFTUP)


def timing():
    timer = threading.Timer(5, auto_fuse)
    timer.start()


def is_bot_on():
    while is_bot == True:
        startclickbot(handle)
    while is_bot == False:
        auto_fuse()

time.sleep(2)
is_running()
is_bot_on()





