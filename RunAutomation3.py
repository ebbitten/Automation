# requires pyauotgui, pyhook,  pillow,
import argparse
import pyautogui, time, winsound
import importlib
import random
import helperLoop
import ocr
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True

MAX_FAILED_MOVE_ATTEMPTS = 15
FAILED_MOVE_ATTEMPTS = 0


def getCoord():
    counter = 0
    prevX = 0
    prevY = 0
    while counter < 5:
        printsleep(.5)
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
    printsleep(5)
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
    printsleep(5)
    while timeElapsed < 20000:
        importlib.reload(helperLoop)
        curTime = time.time()
        timeElapsed = curTime - startTime
        lastHeal = helperLoop.absorpNMZ(coordsList, timeElapsed, startTime, consumedList, consumedCounter, lastHeal,
                                        rapidHeal)
        # print(str(consumedList) + "consumed list")
        if not (overCoords or absorpCoords):
            break


def tanDragonHides(hides, computer="Y570"):
    #TODO fiure out why the 5 mousekey/right clicking doesn't always work
    if computer == "Y570":
        locations = [[677, 139], [1076, 67], [1828, 832], [980, 519], [1751, 783]]
    elif computer == "T470s":
        locations = [[538, 187], [1134, 77], [1781, 723], [989, 506], [1668, 645]]
    else:
        raise ValueError
    phrases = [ "Withdraw-1 Blue dragonhide", "Close",
             "Cast Tan Leather", "Bank Grand Exchange Booth", "Deposit-1 Blue dragon leather" ]
    print('initiating...')
    printsleep(5)
    actionsList = (('easyMove(locations[0], phrases[0])','easyPress("num5")','printsleep(.2)','easyPress("num2")','easyPress("num2")','easyPress("num5")','printsleep(1)'),
                   ('easyMove(locations[1], phrases[1])','easyClick()'),
                   ('easyMove(locations[2], phrases[2])','printsleep(3)','clickWait(6)'),
                   ('easyMove(locations[3], phrases[3])','easyClick()','printsleep(1.2)'),
                   ('easyMove(locations[4])','easyPress("num5")','printsleep(.2)','easyPress("num2")','easyPress("num2")','easyPress("num5")','printsleep(1)')
               )
    for i in range(int(hides//25)):
        actionsListc = actionsList[:]
        print('on hides number: ' + str(i * 25))
        for actions in actionsListc:
            for action in actions:
                print(str(action))

                exec(action)
                printsleep(.21)
            randomSleep()

def craft_dragon_hides(hides, computer="Y570"):
    if computer == "Y570":
        locations = [[677, 139], [1076, 67], [1828, 832], [1007, 519], [1751, 783]]
    elif computer == "T470s":
        locations = [[898, 512], [1136, 78], [1728, 594], [1667, 597], [989, 506], [1667, 648]]
    else:
        raise ValueError
    print('initiating...')
    printsleep(5)
    actionsList = (('easyMove(locations[0])','easyPress("num5")','printsleep(.2)','easyPress("num2")','easyPress("num2")','easyPress("num5")','printsleep(1)'),
                   ('easyMove(locations[1])','easyClick()'),
                   ('easyMove(locations[2])','printsleep(1.2)','easyClick()'),
                   ('easyMove(locations[3])','easyClick()','printsleep(1.2)'),
                   ('easyPress("1")','printsleep(15)'),
                   ('easyMove(locations[4])', 'printsleep(1.2)', 'easyClick()', 'printsleep(1.2)'),
                   ('easyMove(locations[5])','easyPress("num5")','printsleep(.2)','easyPress("num2")','easyPress("num2")', 'easyPress("num5")','printsleep(1)')
               )
    for i in range(int(hides//25)):
        actionsListc = actionsList[:]
        print('on hides number: ' + str(i * 25))
        for actions in actionsListc:
            for action in actions:
                print(str(action))

                exec(action)
                printsleep(.21)
            randomSleep()


def clickWait(num):
    for i in range(num):
        easyClick()
        printsleep(abs(random.normalvariate(1.4, .1)))
        randomSleep()

def randomSleep():
    if random.random() < .01:
        printsleep(abs(random.normalvariate(40,5)))
    if random.random() < .05:
        printsleep(abs(random.normalvariate(7,3)))
    if random.random() < .002:
        print('browsing')
        # helperLoop.randomBrowsing()
        print('browsing not currently implemented')
        #TODO re-implement but make sure it ends up back in the same spot



def easyMove(location, text="", threshold=80, max_attempts=3):
    humanMove(location[0], location[1], 1.2, 8)
    time.sleep(.2)
    global FAILED_MOVE_ATTEMPTS
    global MAX_FAILED_MOVE_ATTEMPTS
    if text:
        attempts = 0
        while attempts < max_attempts:
            if ocr.screen_and_compare(text, threshold):
                return True
            else:
                humanMove(location[0], location[1], .3, 1, jiggle=True)
                printsleep(.5)
                attempts += 1
        if attempts == max_attempts:
            FAILED_MOVE_ATTEMPTS += 1
            print(FAILED_MOVE_ATTEMPTS)
        if FAILED_MOVE_ATTEMPTS >= MAX_FAILED_MOVE_ATTEMPTS:
            raise FailedMoveAttempt('too many failed movements')
        

class FailedMoveAttempt(Exception):
    "Raised when there's too many failed movement attempts"
    pass

def humanMove(finalx, finaly, totalTime, steps, jiggle=False):
    tweens = [pyautogui.easeOutQuad, pyautogui.easeInQuad, pyautogui.easeInOutQuad]
    startingPos = pyautogui.position()
    # If we're already on the spot just go ahead and get ready to click
    if not jiggle:
        if ((abs(finalx - startingPos[0]) + abs(finaly - startingPos[1])) ** .5) < 5:
            return
    # otherwise move there over a series of steps
    #TODO make this look a lot more "human"
    step_variance = 5
    last_variance = 3
    if jiggle:
        last_variance = 5
    for i in range(1, steps + 1):
        tweenChoice = random.choice(tweens)
        x = startingPos[0] * (steps - i) / steps + finalx * (i) / steps
        y = startingPos[1] * (steps - i) / steps + finaly * (i) / steps
        if i < steps:
            x += random.normalvariate(0, step_variance)
            y += random.normalvariate(0, step_variance)
        elif i == steps:
            x += random.normalvariate(0, last_variance)
            y += random.normalvariate(0, last_variance)
        stepTime = totalTime / steps
        pyautogui.moveTo(x, y, stepTime, tweenChoice, None, False)


def easyPress(key):
    pyautogui.press(key, interval = (random.normalvariate(25,5)/100))

def easyClick():
    helperLoop.doClick(clicks=1, duration=(random.normalvariate(25, 3) / 100))

def printsleep(time_to_sleep):
    if time_to_sleep > 2:
        print("time to sleep: ", time_to_sleep)
    time.sleep(time_to_sleep)

#print("initializing")
#runNMZAbsorp("Y570",0, 0, 320, 190 , 10, 14)
# findCoordinates(2,0,0)
# requires pyauotgui, pyhook,  pillow,


# findCoordinates(1,0,0)
tanDragonHides(5000, computer="Y570")

# craft_dragon_hides(12000, computer="T470s")

#521xhz4FRkTc