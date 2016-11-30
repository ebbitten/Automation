#requires pyauotgui, pyhook,  pillow,
import argparse
import pyautogui,time,winsound
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

def getCoord():
    counter=0
    prevX=0
    prevY=0
    while counter<5:
        time.sleep(.5)
        curposition=pyautogui.position()
        curX=curposition[0]
        curY=curposition[1]
        if curX==prevX and curY==prevY:
            counter+=1
            x = curX
            y = curY
        prevX = curX
        prevY = curY
    winsound.Beep(2500,1000)
    return [x,y]

def findCoordinates(hw,overLoads,prayerpots):
    #assume that the first position is holy wrench
    #the second through 8th position are overloads
    #the 9th through 28th position are prayer pots
    hwCoords=[]
    overCoords=[]
    ppCords=[]
    time.sleep(5)
    for i in range(hw):
        newCoord=getCoord()
        hwCoords.append(newCoord)
    for i in range(overLoads):
        newCoord=getCoord()
        overCoords.append(newCoord)
    for i in range(prayerpots):
        newCoord=getCoord()
        ppCords.append(newCoord)
    winsound.Beep(2000,2000)
    print(hwCoords)
    print(overCoords)
    print(ppCords)
    filePath = input("please input a filepath to save the coordinates")

# findCoordinates(1,7,20)

def runNMZ(oversConsumed=0, ppConsumed=0,overConsumeCounter=310, ppConsumeCounter = 153):
    #TODO upload to Github and start running on other computer
    #Todo: put all coords in one array and then split them based on input
    #TODO load positions from a file
    import helperLoop

    startTime = time.time()
    curTime = time.time()
    overCoords = [[878, 254], [921, 253], [961, 251], [832, 293], [876, 290], [917, 290], [960, 292]]
    ppCoords = [[835, 325], [876, 328], [917, 326], [958, 326], [835, 362], [875, 361], [917, 365], [960, 363], [834, 400], [878, 400], [918, 400], [958, 399], [833, 436], [878, 436], [917, 435], [958, 433], [833, 465], [877, 470], [916, 471], [958, 471]]
    consumedCounter = [overConsumeCounter,ppConsumeCounter]
    if oversConsumed>0:
        for i in range(oversConsumed//4):
            overCoords.pop(0)
    if ppConsumed>0:
        for i in range(ppConsumed//4):
            ppCoords.pop(0)
    if ppConsumed>0 or oversConsumed>0:
        timeElapsed=max(ppConsumed*153,oversConsumed*305)
        startTime=curTime-timeElapsed
    coordsList = [overCoords,ppCoords]
    timeElapsed = curTime-startTime
    consumedList = [oversConsumed,ppConsumed]
    print("starting in 10")
    while timeElapsed<9000:
        importlib.reload(helperLoop)
        curTime=time.time()
        timeElapsed = curTime - startTime
        helperLoop.meleeNMZ(coordsList,timeElapsed,startTime,consumedList,consumedCounter)
        #print(str(consumedList) + "consumed list")
#requires pyauotgui, pyhook,  pillow
import argparse
import pyautogui,time,winsound,random
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
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



def checkAndConsume(consumedType,consumedTimer,coordsList,consumedList,timeElapsed):
    if timeElapsed - consumedTimer[consumedType] * consumedList[consumedType] > consumedTimer[consumedType]:
        typename = ["Overload","Prayer Potion"]
        print(("Drinking " + str(typename[consumedType])+"\n")*3)
        time.sleep(2)
        #move to our potion
        x = coordsList[consumedType][0][0] +random.randint(-3,3)
        y = coordsList[consumedType][0][1] +random.randint(-3,3)
        moveTime = random.randrange(30,50,1)/10
        humanMove(x, y, moveTime, 6)
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
        moveTime = random.randrange(30, 50, 1) / 10
        humanMove(x, y, moveTime, 6)
        #update our consumption
        consumedList[consumedType] += 1
        if consumedList[consumedType] % 4 == 0:
            coordsList[consumedType].pop(0)





print("initializing")
runNMZ(11,30)





