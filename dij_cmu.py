# class point:
#     def __init__ (self,name,x,y):
#         self.name = name
#         self.cor = (x,y)

import math

# A = point("A",10,30)
# B = point("B",10,10)
# C = point("C",20,30)
# D = point("D",30,30)

# points = [A,B,C,D]

# d = {
#     A:(B,C),
#     B:(A,C,D),
#     C:(A,B,D),
#     D:(C,B)
# }

from dataset import getData
from place_identifier import *

points, cmap = getData()

start, end = getArea('WEH 6330','WEH 8100')

for p in points:
    if p.name == start:
        startPoint = p
    elif p.name == end:
        endPoint = p
    else:
        pass


def dij(graph, start, end):
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
    print(shortest_dis)
    print(predecessor)

    currentNode = end
    while currentNode != start:
        try:
            path.insert(0, currentNode.name)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('This path is unreachable')
    path.insert(0, start.name)
    print(path)

dij(cmap, startPoint, endPoint)
