#adj list
def bfs(graph,visited,queue):
    while(queue):
        node,parent = queue.pop(0)
        # visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)      
                queue.append([neighbour,node])
            elif neighbour!=parent:
                return True
    return False

def cycleDetectBfs(graph):
    V = len(graph)
    visited = set()
    queue = []
    for node in range(V):
        if node not in visited:
            queue.append([node,-1])
            visited.add(node)      
            if(bfs(graph,visited,queue)):
                return True
    return False

#when putting inside queue then mark as visited.
# not when popping from queue , otherwise dual entry in case of triangle graph 0,1,2

#test cases single node no edge
#self loop

#adj matrix

def bfsmatrix(graph,visited,queue):
def cycleBfsMatrix(graph):
    V = len(graph)
    queue = []
    visite = set()
    for node in range(V):
        if ()