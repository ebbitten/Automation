# requires pyauotgui, pyhook,  pillow,
import argparse
import pyautogui, time, winsound
import importlib
import random
import helperLoop
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True


def getCoord():
    counter = 0
    prevX = 0
    prevY = 0
    while counter < 5:
        time.sleep(.5)
        curposition = pyautogui.position()
        curX = curposition[0]
        curY = curposition[1]
        if curX == prevX and curY == prevY:
            counter += 1
            x = curX
            y = curY
        prevX = curX
        prevY = curY
    winsound.Beep(2500, 1000)
    return [x, y]


def findCoordinates(hw, overLoads, prayerpots):
    # assume that the first position is holy wrench
    # the second through 8th position are overloads
    # the 9th through 28th position are prayer pots
    hwCoords = []
    overCoords = []
    ppCords = []
    time.sleep(5)
    for i in range(hw):
        newCoord = getCoord()
        hwCoords.append(newCoord)
    for i in range(overLoads):
        newCoord = getCoord()
        overCoords.append(newCoord)
    for i in range(prayerpots):
        newCoord = getCoord()
        ppCords.append(newCoord)
    winsound.Beep(2000, 2000)
    print(hwCoords)
    print(overCoords)
    print(ppCords)
    filePath = input("please input a filepath to save the coordinates")


# findCoordinates(1,0,0)

def runNMZ(oversConsumed=0, ppConsumed=0, overConsumeCounter=310, ppConsumeCounter=150):
    # TODO upload to Github and start running on other computer
    # Todo: put all coords in one array and then split them based on input
    # TODO load positions from a file
    import helperLoop

    startTime = time.time()
    curTime = time.time()
    overCoords = [[1195, 256], [1237, 259], [1280, 256], [1155, 288], [1194, 294], [1235, 295], [1279, 292]]
    ppCoords = [[1155, 330], [1194, 329], [1238, 331], [1279, 333], [1155, 368], [1198, 368], [1238, 369], [1280, 365],
                [1155, 405], [1197, 404], [1239, 402], [1278, 403], [1152, 438], [1196, 438], [1235, 442], [1281, 441],
                [1154, 477], [1194, 477], [1239, 474], [1280, 476]]
    rapidHeal = [1293, 295]
    consumedCounter = [overConsumeCounter, ppConsumeCounter]
    if oversConsumed > 0:
        for i in range(oversConsumed // 4):
            overCoords.pop(0)
    if ppConsumed > 0:
        for i in range(ppConsumed // 4):
            ppCoords.pop(0)
    if ppConsumed > 0 or oversConsumed > 0:
        timeElapsed = max(ppConsumed * 153, oversConsumed * 305)
        startTime = curTime - timeElapsed
    coordsList = [overCoords, ppCoords]
    timeElapsed = curTime - startTime
    consumedList = [oversConsumed, ppConsumed]
    print("starting in 10")
    while timeElapsed < 12000:
        importlib.reload(helperLoop)
        curTime = time.time()
        timeElapsed = curTime - startTime
        helperLoop.meleeNMZ(coordsList, timeElapsed, startTime, consumedList, consumedCounter)
        # print(str(consumedList) + "consumed list")


def runNMZAbsorp(laptopType = "Y570", oversConsumed=0, absorpConsumed=0, overConsumeCounter=320, absorpConsumeCounter=160, numOvers=10, numAbsorps=16):
    # TODO upload to Github and start running on other computer
    # Todo: put all coords in one array and then split them based on input
    # TODO load positions from a file
    #TODO initialize should include getting your HP down
    import helperLoop
    #start timer
    startTime = time.time()
    curTime = time.time()
    lastHeal = time.time()

    #determine the coordinate set we're using
    if laptopType == "Y570":
        invenCoords = [[1195, 256], [1237, 259], [1280, 256], [1155, 288], [1194, 294], [1235, 295], [1279, 292],
                       [1155, 330], [1194, 329], [1238, 331], [1279, 333], [1155, 368], [1198, 368], [1238, 369],
                       [1280, 365], [1155, 405],[1197, 404], [1239, 402], [1278, 403], [1152, 438], [1196, 438],
                       [1235, 442], [1281, 441],[1154, 477], [1194, 477], [1239, 474], [1280, 476]]
        rapidHeal = [1293, 295]
    else:
        invenCoords = [[878, 254], [921, 253], [961, 251], [832, 293],[876, 290], [917, 290], [960, 292],
                   [835, 325], [876, 328], [917, 326], [958, 326], [835, 362], [875, 361], [917, 365],
                   [960, 363], [834, 400], [878, 400], [918, 400], [958, 399],[833, 436], [878, 436],
                   [917, 435], [958, 433], [833, 465], [877, 470], [916, 471], [958, 471]]
        rapidHeal = [971, 288]


    #parse that coordinate let into arrays that we'll use to loop over    
    overCoords = invenCoords[:numOvers]
    absorpCoords = invenCoords[numOvers:numAbsorps+numOvers]
    #update consumed counter if we passed any in
    consumedCounter = [overConsumeCounter, absorpConsumeCounter]
    #decrement the amount that we have left based on our consumed counter
    if oversConsumed > 0:
        for i in range(oversConsumed // 4):
            overCoords.pop(0)
    if absorpConsumed > 0:
        for i in range(absorpConsumed // 4):
            absorpCoords.pop(0)

    #update how much time had previously passed based on the consumed counter
    if absorpConsumed > 0 or oversConsumed > 0:
        timeElapsed = max(absorpConsumed * absorpConsumeCounter, oversConsumed * overConsumeCounter)
        startTime = curTime - timeElapsed
    #make our coordinate list that we'll loop over
    coordsList = [overCoords, absorpCoords]
    #initialzie time elapsed
    timeElapsed = curTime - startTime
    #Make the list for how many we'll consider consumed
    consumedList = [oversConsumed, absorpConsumed]
    print("starting in 5")
    time.sleep(5)
    while timeElapsed < 20000:
        importlib.reload(helperLoop)
        curTime = time.time()
        timeElapsed = curTime - startTime
        lastHeal = helperLoop.absorpNMZ(coordsList, timeElapsed, startTime, consumedList, consumedCounter, lastHeal,
                                        rapidHeal)
        # print(str(consumedList) + "consumed list")
        if not (overCoords or absorpCoords):
            break


def tanDragonHides(hides):
    locations = [[677, 139], [1076, 67], [1828, 832], [1007, 519], [1751, 783]]
    print('initiating...')
    time.sleep(5)
    actionsList = (('easyMove(locations[0])','easyPress("num5")','time.sleep(.2)','easyPress("num2")','easyPress("num2")','easyPress("num5")','time.sleep(1)'),
                   ('easyMove(locations[1])','easyClick()'),
                   ('easyMove(locations[2])','time.sleep(3)','clickWait(6)'),
                   ('easyMove(locations[3])','easyClick()','time.sleep(1.2)'),
                   ('easyMove(locations[4])','easyPress("num5")','time.sleep(.2)','easyPress("num2")','easyPress("num2")','easyPress("num5")','time.sleep(1)')
               )
    for i in range(int(hides//25)):
        actionsListc = actionsList[:]
        print('on hides number: ' + str(i * 25))
        for actions in actionsListc:
            for action in actions:
                print(str(action))

                exec(action)
            randomSleep()

def clickWait(num):
    for i in range(num):
        easyClick()
        time.sleep(abs(random.normalvariate(1.4, .1)))
        randomSleep()

def randomSleep():
    if random.random() < .01:
        time.sleep(abs(random.normalvariate(40,5)))
    if random.random() < .1:
        time.sleep(abs(random.normalvariate(7,3)))
    if random.random() < .002:
        print('browsing')
        helperLoop.randomBrowsing()

def easyMove(location):
    helperLoop.humanMove(location[0],location[1],1.2,8)

def easyPress(key):
    pyautogui.press(key, interval = (random.normalvariate(25,5)/100))

def easyClick():
    helperLoop.doClick(clicks=1, duration=(random.normalvariate(25, 3) / 100))

#print("initializing")
#runNMZAbsorp("Y570",0, 0, 320, 190 , 10, 14)
#findCoordinates(1,0,0)
# requires pyauotgui, pyhook,  pillow,

tanDragonHides(5000)


#521xhz4FRkTc