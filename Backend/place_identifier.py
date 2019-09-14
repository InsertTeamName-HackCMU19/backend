# wean floor 5-8; second digit 0-5;
def getWeanPoint(inp,Building,spaceIdx):
    floor = -1
    area = ''
    for i in range(5,9):
        if int(inp[spaceIdx+1:spaceIdx+2]) == i:
            floor = i
            break
    assert(floor != -1)
    secondDigit = int(inp[spaceIdx+2:spaceIdx+3])
    if secondDigit == 3:
        area = 'NE'
    elif secondDigit == 4:
        area = 'SE'
    elif secondDigit == 1:
        area = 'SW'
    elif secondDigit == 2:
        area = 'NW'
    elif secondDigit == 0:
        area = 'ST'
    elif secondDigit == 5:
        area = 'ST'
    return Building + '_' + str(floor) + '_' + area

# ghc floor 4-5; second digit 0-4, 012457;
def getGhcPoint(inp,Building,spaceIdx):
    floor = -1
    area = '..'
    for i in range(4,6):
        if int(inp[spaceIdx+1:spaceIdx+2]) == i:
            floor = i
    assert(floor != -1)
    secondDigit = int(inp[spaceIdx+2:spaceIdx+3])
    # print(secondDigit)
    # floor 4
    if floor == 4:
        if secondDigit == 4:
            area = 'NW'
        elif secondDigit == 3:
            area = 'NE'
        elif secondDigit == 1:
            area = 'SW'
        elif secondDigit == 0 or secondDigit == 2:
            area = 'SE'
    # floor 5
    elif floor == 5:
        if secondDigit == 4 or secondDigit == 7:
            area = 'NW'
        elif secondDigit == 5:
            area = 'NE'
        elif secondDigit == 0 or secondDigit == 1:
            area = 'SW'
        elif secondDigit == 2:
            area = 'SE'

    return Building + '_' + str(floor) + '_' + area

# get the area of the point
def getArea(inputStart, inputEnd):
    S_and_E = [inputStart, inputEnd]
    Out_S_and_E = []
    for inp in S_and_E:
        spaceIdx = inp.index(' ')
        Building = inp[0:spaceIdx]
        if Building == 'WEH':
            Out_S_and_E.append(getWeanPoint(inp,Building,spaceIdx))

        elif Building == 'GHC':
            Out_S_and_E.append(getGhcPoint(inp,Building,spaceIdx))

        elif Building == 'NSH':
            pass
    return Out_S_and_E[0],Out_S_and_E[1]


# print(getArea('GHC 5730','WEH 6330'))
# print(getArea('WEH 7400','GHC 4300'))
# print(getArea('WEH 7400','GHC 5700'))
