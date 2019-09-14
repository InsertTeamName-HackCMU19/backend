def getWeanPoint(inp,Building,spaceIdx):
    floor = -1
    area = ''
    for i in range(4,9):
        if int(inp[spaceIdx+1:spaceIdx+2]) == i:
            floor = i
            break
    assert(floor != -1)
    if int(inp[spaceIdx+2:spaceIdx+3]) == 3:
        area = 'NE'
    elif int(inp[spaceIdx+2:spaceIdx+3]) == 4:
        area = 'SE'
    elif int(inp[spaceIdx+2:spaceIdx+3]) == 1:
        area = 'SW'
    elif int(inp[spaceIdx+2:spaceIdx+3]) == 2:
        area = 'NW'
    elif int(inp[spaceIdx+2:spaceIdx+3]) == 0:
        area = 'ST'

    return Building + '_' + str(floor) + '_' + area

def getArea(inputStart, inputEnd):
    spaceIdx = inputEnd.index(' ')
    Building = inputStart[0:spaceIdx]
    # if the building is in WEH
    if Building == 'WEH':
        weanStart = getWeanPoint(inputStart,Building,spaceIdx)
        weanEnd = getWeanPoint(inputEnd,Building,spaceIdx)
        return weanStart, weanEnd
    elif Building == 'GHC':
        pass
    elif Building == 'NSH':
        pass

# print(getArea('WEH 6330','WEH 8100'))