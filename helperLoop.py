#requires pyauotgui, pyhook,  pillow
import argparse
import pyautogui,time,winsound,random
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

def meleeNMZ(coordsList,timeElapsed,startTime,consumedList,consumedTimer):
    time.sleep(10)
    curTime = time.time()
    timeElapsed = curTime - startTime
    print("time elapsed is " + str(timeElapsed))
    # Check if we should drink a prayerpot
    # a prayer dose restores 154 seconds of prayer
    #0 is over, 1 is pp
    for i in range(2):
        checkAndConsume(i, consumedTimer, coordsList, consumedList, timeElapsed)



def checkAndConsume(consumedType,consumedTimer,coordsList,consumedList,timeElapsed):
    if timeElapsed - consumedTimer[consumedType] * consumedList[consumedType] > consumedTimer[consumedType]:
        typename = ["Overload","Prayer Potion"]
        print(("Drinking " + str(typename[consumedType])+"\n")*3)
        time.sleep(2)
        #move to our potion
        x = coordsList[consumedType][0][0] +random.randint(-3,3)
        y = coordsList[consumedType][0][1] +random.randint(-3,3)
        moveTime = random.randrange(50,80,1)/10
        pyautogui.moveTo(x, y, moveTime, pyautogui.easeInElastic)
        #click
        try:
            pyautogui.click()
        except:
            try:
                pyautogui.click()
            except:
                pass
        screenWidth, screenHeight = pyautogui.size()
        #Move to a random location
        x = random.randint(1,screenWidth)
        y = random.randint(1,screenHeight)
        moveTime = random.randrange(50, 80, 1) / 10
        pyautogui.moveTo(x, y, moveTime, pyautogui.easeInOutQuad)
        #update our consumption
        consumedList[consumedType] += 1
        if consumedList[consumedType] % 4 == 0:
            coordsList[consumedType].pop(0)



def extraStuff():
    # screenWidth, screenHeight = pyautogui.size()
    # currentMouseX, currentMouseY = pyautogui.position()
    # pyautogui.moveTo(100, 150)
    # pyautogui.click()
    # pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
    # pyautogui.doubleClick()
    # pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.tweens.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
    # pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
    # pyautogui.press('esc')
    # pyautogui.keyDown('shift')
    # pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
    # pyautogui.keyUp('shift')
    # pyautogui.hotkey('ctrl', 'c')
    pass

    # if timeElapsed - 154 * consumedList[1] > 154:
    #     print("drinking prayer")
    #     time.sleep(2)
    #     x = ppCoords[0][0] +random.randint(-3,3)
    #     y = ppCoords[0][1] +random.randint(-3,3)
    #     moveTime = random.randrange(3,5,.1)
    #     pyautogui.moveTo(x, y, moveTime)
    #     try:
    #         pyautogui.click()
    #     except:
    #         try:
    #             pyautogui.click()
    #         except:
    #             pass
    #     consumedList[1] += 1
    #     if consumedList[1] % 4 == 0:
    #         ppCoords.pop(0)
    # if timeElapsed - 305 * consumedList[0] >= 0:
    #     print("drinking over")
    #     time.sleep(2)
    #     x = overCoords[0][0] +random.randint(-3,3)
    #     y = overCoords[0][1] +random.randint(-3,3)
    #     moveTime = random.randrange(3,5,.1)
    #     pyautogui.moveTo(x, y, moveTime)
    #     try:
    #         pyautogui.click()
    #     except:
    #         try:
    #             pyautogui.click()
    #         except:
    #             pass
    #     consumedList[0] += 1
    #     if consumedList[0] % 4 == 0:
    #         overCoords.pop(0)