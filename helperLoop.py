#requires pyauotgui, pyhook,  pillow
import argparse
import pyautogui,time,winsound,random
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False
def humanMove(finalx,finaly,totalTime,steps):
    tweens = [pyautogui.easeOutQuad,pyautogui.easeInQuad,pyautogui.easeInOutQuad]
    startingPos=pyautogui.position()
    for i in range(1,steps+1):
        tweenChoice=random.choice(tweens)
        x = startingPos[0]*(steps-i)/steps + finalx * (i)/steps
        y = startingPos[1]*(steps-i)/steps + finaly * (i)/steps
        if i<steps:
            x+=random.randint(-20,20)
            y+=random.randint(-20,20)
        stepTime = totalTime/steps
        pyautogui.moveTo(x,y,stepTime,tweenChoice,None,False)

def meleeNMZ(coordsList,timeElapsed,startTime,consumedList,consumedTimer):
    time.sleep(10)
    curTime = time.time()
    timeElapsed = curTime - startTime
    print("time elapsed is " + str(timeElapsed))
    # Check if we should drink a prayerpot
    # a prayer dose restores 154 seconds of prayer
    #0 is over, 1 is pp
    for i in range(2):
        if coordsList[i]:
            checkAndConsume(i, consumedTimer, coordsList, consumedList, timeElapsed)

def absorpNMZ(coordsList,timeElapsed,startTime,consumedList,consumedTimer,lastHeal,rapidHeal):
    time.sleep(1)
    curTime = time.time()
    timeElapsed = curTime - startTime
    print("time elapsed is " + str(timeElapsed))
    # Check if we should drink a prayerpot
    # a prayer dose restores 154 seconds of prayer
    #0 is over, 1 is pp
    for i in range(2):
        if coordsList[i]:
            checkAndConsume(i, consumedTimer, coordsList, consumedList, timeElapsed)
    if time.time() - lastHeal >40:
        flickPray(rapidHeal)
        lastHeal=time.time()
    return lastHeal



def checkAndConsume(consumedType,consumedTimer,coordsList,consumedList,timeElapsed):
    if timeElapsed - consumedTimer[consumedType] * consumedList[consumedType] > consumedTimer[consumedType]:
        typename = ["Overload","Prayer Potion"]
        print(("Drinking " + str(typename[consumedType])+"\n")*3)
        time.sleep(2)
        #move to our potion
        x = coordsList[consumedType][0][0] +random.randint(-3,3)
        y = coordsList[consumedType][0][1] +random.randint(-3,3)
        moveTime = random.randrange(20,40,1)/10
        humanMove(x, y, moveTime, 6)
        #click
        doClick()
        screenWidth, screenHeight = pyautogui.size()
        #Move to a random location
        x = random.randint(1,screenWidth)
        y = random.randint(1,screenHeight)
        moveTime = random.randrange(30, 50, 1) / 10
        humanMove(x, y, moveTime, 6)
        #update our consumption
        consumedList[consumedType] += 1
        if consumedList[consumedType] % 4 == 0:
            coordsList[consumedType].pop(0)

def flickPray(rapidHeal):
    randInterval = random.randint(15,25)/100
    pyautogui.typewrite('f5', interval=randInterval)
    randInterval = random.randint(15, 25) / 10
    humanMove(rapidHeal[0],rapidHeal[1],randInterval,2)
    doClick()
    randInterval = random.randint(15, 25) / 100
    time.sleep(randInterval)
    doClick()


def doClick():
    try:
        pyautogui.click()
    except:
        try:
            pyautogui.click()
        except:
            pass

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