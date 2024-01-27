from scripts.scripts import B


import time
def last_heal_time(coords_list, time_elapsed, start_time, consumed_list, consumed_timer, last_heal, rapid_heal):
    time.sleep(1)
    curTime = time.time()
    time_elapsed = curTime - start_time
    print("time elapsed is " + str(time_elapsed))
    # Check if we should drink a prayerpot
    # a prayer dose restores 154 seconds of prayer
    # 0 is over, 1 is pp
    for i in range(2):
        if coords_list[i]:
            B.check_and_consume(i, consumed_timer, coords_list, consumed_list, time_elapsed)
    if time.time() - last_heal > 30:
        B.flick_pray(rapid_heal)
        last_heal = time.time()
    return last_heal


def runNMZAbsorp(laptopType="Desktop", oversConsumed=0, absorpConsumed=0, overConsumeCounter=310, absorpConsumeCounter=600,
                 numOvers=10, numAbsorps=16):
    # TODO load positions from a file
    # TODO initialize should include getting your HP down
    # start timer
    startTime = time.time()
    curTime = time.time()
    lastHeal = time.time()
    # determine the coordinate set we're using
    if laptopType == "Y570":
        invenCoords = [[1195, 256], [1237, 259], [1280, 256], [1155, 288], [1194, 294], [1235, 295], [1279, 292],
                       [1155, 330], [1194, 329], [1238, 331], [1279, 333], [1155, 368], [1198, 368], [1238, 369],
                       [1280, 365], [1155, 405], [1197, 404], [1239, 402], [1278, 403], [1152, 438], [1196, 438],
                       [1235, 442], [1281, 441], [1154, 477], [1194, 477], [1239, 474], [1280, 476]]
        rapidHeal = [1293, 295]
    else:
        invenCoords = [[1700,  808], [1744,  808], [1786,  812], [1826,  812], [1701, 849], [1744, 850], [1785, 851],
                       [1828, 849], [1700, 886], [1742, 883], [1784, 882], [1827, 886], [1700, 921], [1744, 921],
                       [1785, 917], [1827, 919], [1699, 955], [1743, 955], [1785, 958], [1825, 956], [1699, 991],
                       [1742, 990], [1783, 990], [1825, 992], [1702, 1030], [1742, 1028], [1782, 1027], [1832, 1028]]

        rapidHeal = [1835, 843]


    # parse that coordinate let into arrays that we'll use to loop over
    overCoords = invenCoords[:numOvers]
    absorpCoords = invenCoords[numOvers:numAbsorps + numOvers]
    # update consumed counter if we passed any in
    consumedCounter = [overConsumeCounter, absorpConsumeCounter]
    # decrement the amount that we have left based on our consumed counter
    if oversConsumed > 0:
        for i in range(oversConsumed // 4):
            overCoords.pop(0)
    if absorpConsumed > 0:
        for i in range(absorpConsumed // 4):
            absorpCoords.pop(0)
    # update how much time had previously passed based on the consumed counter
    if absorpConsumed > 0 or oversConsumed > 0:
        timeElapsed = max(absorpConsumed * absorpConsumeCounter, oversConsumed * overConsumeCounter)
        startTime = curTime - timeElapsed
    # make our coordinate list that we'll loop over
    coordsList = [overCoords, absorpCoords]
    # initialzie time elapsed
    timeElapsed = curTime - startTime
    # Make the list for how many we'll consider consumed
    consumedList = [oversConsumed, absorpConsumed]
    print("starting in 5")
    B.print_sleep(5)
    while timeElapsed < 30000:
        curTime = time.time()
        timeElapsed = curTime - startTime
        lastHeal = last_heal_time(coordsList, timeElapsed, startTime, consumedList, consumedCounter, lastHeal,
                                  rapidHeal)
        # print(str(consumedList) + "consumed list")
        if not (overCoords or absorpCoords):
            break