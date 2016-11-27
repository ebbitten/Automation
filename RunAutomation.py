#requires pyauotgui, pyhook,  pillow,
import argparse
import pyautogui,time,winsound,importlib
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

print("initializing")
runNMZ(11,30)





