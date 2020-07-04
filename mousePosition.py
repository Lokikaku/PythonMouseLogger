import pyautogui
import time
import keyboard

noYeet = True
period = "."
try:
    while noYeet:
        x, y = pyautogui.position()
        xArchive = x
        yArchive = y
        time.sleep(0.1)
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(xArchive) + ' Y: ' + str(yArchive)
        if x != xArchive:
            with open('mousePos1.txt', 'a') as f:
                f.write(positionStr)
                f.write("\n")
        else:
            with open('mousePos1.txt', 'a') as f:
                f.write(period)
                f.write("\n")
        if keyboard.is_pressed('esc'): 
            break
        else:
            pass
        if keyboard.is_pressed('p'): 
            noYeet = False
        else:
            pass
except KeyboardInterrupt:
    print('\n')
# Hopefully this edit works :P and ads an escape route if things go south, which yes, they can.
