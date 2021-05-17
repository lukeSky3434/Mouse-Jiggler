import pyautogui, sys
from datetime import datetime
import time, threading


#Installation
#py -m pip install pyautogui

def execute_login():
    print('login at {}'.format(datetime.now))

def execute_logout():
    print('logout at {}'.format(datetime.now))


def main():
    print(pyautogui.position())
    size = pyautogui.size()
    print(size)

    width = size.width / 2 
    height = size.height / 2 

    startx = width + 200
    starty = height + 100
    endx = size.width - 20
    endy = size.height - 20
    xit = 240
    yit = 120
    num_seconds = 0.5
    x = startx
    y = starty

    pyautogui.moveTo(x, y, duration=0)
    pyautogui.click(x, y)

    print('Initialized Successfully at {}'.format(datetime.now()))

    while True:

        x = x + xit
        y = y + yit
        if(x > endx or x < startx):
            x = startx
        if(y > endy or y < starty):
            y = starty
        pyautogui.moveTo(x, y, duration=num_seconds)

        time.sleep(5)

        if(x + xit > endx):
            pyautogui.click(x, y)

if __name__ == "__main__":
    main()
