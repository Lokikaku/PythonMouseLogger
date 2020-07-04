import pyautogui
import time

noYeet = True
period = "."
try:
    while noYeet:
        x, y = pyautogui.position()
        xArchive = x
        yArchive = y
        time.sleep(0.2)
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
except KeyboardInterrupt:
    print('\n')
