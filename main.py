from pyautogui import size, moveTo, click
from time import sleep

winSize = size()
print("v2.1")
print("Keeping you online...")

while (1 == 1):
    moveTo(winSize[0]/2, winSize[1]/2, 1)
    click()
    print("Clicked!")
    sleep(60)