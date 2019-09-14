import math
from dataset import getData
from place_identifier import *

def findPath(S, E):
    points, cmap = getData()
    start, end = getArea(S,E)

    for p in points:
        if p.name == start:
            startPoint = p
        elif p.name == end:
            endPoint = p
        else:
            pass

    print(startPoint, endPoint)

    return dij(cmap, startPoint, endPoint)

def dij(graph, start, end):
    # if user start and end at the same place:
    if start == end:
        return [start]
    
    shortest_dis = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []

    for node in unseenNodes:
        shortest_dis[node] = infinity
    shortest_dis[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_dis[node] < shortest_dis[minNode]:
                minNode = node
        weight = 0
        for adj in graph[minNode]:
            weight = math.sqrt((minNode.cor[0]-adj.cor[0])**2 + (minNode.cor[1]-adj.cor[1])**2)
            if weight + shortest_dis[minNode] < shortest_dis[adj]:
                shortest_dis[adj] = weight + shortest_dis[minNode]
                predecessor[adj] = minNode
        unseenNodes.pop(minNode)

    currentNode = end
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            return 'This path is unreachable'
    path.insert(0, start)
    s_path = []
    for po in path:
        s_path.append(po.serialize())
    return (s_path)