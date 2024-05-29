import time
import pyautogui as auto
time.sleep(3)
with open('theText.txt', 'r') as theFile:
    auto.FAILSAFE = False
    for line in theFile:
        auto.typewrite(line)
        auto.press('enter')
        time.sleep(0.5)