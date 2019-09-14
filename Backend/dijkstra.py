cmap = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}

def dijkstra(graph, start, end):
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
        
        for childnode, weight in graph[minNode].items():
            if weight + shortest_dis[minNode] < shortest_dis[childnode]:
                shortest_dis[childnode] = weight + shortest_dis[minNode]
                predecessor[childnode] = minNode
        unseenNodes.pop(minNode)
    print(shortest_dis)
    print(predecessor)

    currentNode = end
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('This path is unreachable')
    print(path)

dijkstra(cmap, 'a', 'd')
