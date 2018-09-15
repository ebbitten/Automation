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
    if time.time() - lastHeal >30:
        flickPray(rapidHeal)
        lastHeal=time.time()
    return lastHeal



def checkAndConsume(consumedType,consumedTimer,coordsList,consumedList,timeElapsed):
    if timeElapsed - consumedTimer[consumedType] * consumedList[consumedType] > consumedTimer[consumedType]:
        typename = ["Overload","Prayer Potion"]
        print(("Drinking " + str(typename[consumedType])+"\n")*3)
        time.sleep(2)
        #move to our potion
        x = coordsList[consumedType][0][0] +random.normalvariate(0,2)
        y = coordsList[consumedType][0][1] +random.normalvariate(0,2)
        moveTime = random.randrange(20,40,1)/10
        humanMove(x, y, moveTime, 3)
        #click
        doClick(duration=random.normalvariate(20,3)/100)
        time.sleep(.5)
        #Move to a random location occasionly
        if random.randint(0,20) > 19:
            randomBrowsing()
        #update our consumption
        consumedList[consumedType] += 1
        if consumedList[consumedType] % 4 == 0:
            coordsList[consumedType].pop(0)
        if typename[consumedType]=="Overload" and len(coordsList[consumedType])==1 and consumedList[consumedType] % 4 == 3:
            coordsList[consumedType].pop(0)
            consumedList[consumedType] += 1

def flickPray(rapidHeal):
    randInterval = random.randint(20,30)/100
    pyautogui.press('f5', interval=randInterval)
    time.sleep(random.randint(25, 35) / 100)
    randInterval = random.normalvariate(25, 3) / 10
    humanMove(rapidHeal[0],rapidHeal[1],randInterval,2)
    doClick(clicks = 1, duration = (random.normalvariate(25, 3)/100))
    time.sleep(random.randint(150, 200) / 100)
    doClick(clicks=1, duration=(random.normalvariate(25, 3) / 100))
    time.sleep(random.normalvariate(175,15)/100)
    randInterval = random.normalvariate(25, 3) / 100
    pyautogui.press('esc', interval=randInterval)


def humanMove(finalx,finaly,totalTime,steps):
    tweens = [pyautogui.easeOutQuad,pyautogui.easeInQuad,pyautogui.easeInOutQuad]
    startingPos=pyautogui.position()
    #If we're already on the spot just go ahead and get ready to click
    if ((abs(finalx - startingPos[0])+abs(finaly - startingPos[1]))**.5) < 5:
        return
    #otherwise move there over a series of steps
    for i in range(1,steps+1):
        tweenChoice=random.choice(tweens)
        x = startingPos[0]*(steps-i)/steps + finalx * (i)/steps
        y = startingPos[1]*(steps-i)/steps + finaly * (i)/steps
        if i < steps:
            x +=random.normalvariate(0,5)
            y +=random.normalvariate(0,5)
        elif i == steps:
            x += random.normalvariate(0,3)
            y += random.normalvariate(0,3)
        stepTime = totalTime/steps
        pyautogui.moveTo(x,y,stepTime,tweenChoice,None,False)

def doClick(clicks=1, interval=0.0, button='left', duration=0.0,):
    try:
        pyautogui.click(clicks=clicks, interval = interval, button = button, duration = duration)
    except:
        try:
            pyautogui.click(clicks=clicks, interval=interval, button=button, duration=duration)
        except:
            pass

def randomBrowsing():
    screenWidth, screenHeight = pyautogui.size()
    x = random.randint(1,screenWidth)
    y = random.randint(1,screenHeight)
    moveTime = random.randrange(15, 30, 1) / 10
    humanMove(x, y, moveTime, 4)

def sellStuff(times):
    #needs numkeys///osBuddy on with distance = 90
    for t in range(times):
        print('sold ','\n',t)
        doClick(button='right',duration=(random.randint(20, 30)/100))
        time.sleep(random.randint(20,30)/100)
        pyautogui.press('num2', interval = random.randint(20,30)/100)
        pyautogui.press('num5', interval=random.randint(20, 30) / 100)
        pyautogui.press('num8', interval=random.randint(20, 30) / 100)
        time.sleep(random.randint(20, 30) / 100)
        if .9 < random.random():
            time.sleep(random.randint(10,30)/10)
        if .98 < random.random():
            time.sleep(random.randint(8,15))




def doAndShortSleep(func, length = random.randint(20,30)/100):
    pass
    #figure out how to return/curry/partial/whatever a function that has its original
    # feature but also sleeps for a little

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
