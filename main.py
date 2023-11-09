from pyautogui import size, press, write, moveTo, click
from time import sleep
#import pyautogui, time

winSize = size()
press("win")
sleep(2.5)
write("Microsoft Teams classic (work or school)")
sleep(2.5)
press("enter")
sleep(5)

while (1 == 1):
    moveTo(winSize[0]/5, 32, 1)
    click()
    print()
    sleep(60)