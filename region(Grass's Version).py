#Grass' region finder, This has already been replaced in main.
#Use that one instead

import pyautogui
import win32api
import time
a = -1
print("Press F7 to get mouse position (x, y)")

while True:
    x = 0
    y = 0
    x, y = pyautogui.position()
    a = win32api.GetKeyState(0x76)
    if a < 0:
        print(str(x)+ ", " + str(y)+ ", ")
    time.sleep(0.1)
