#do dfs and check at each step if neighbour in visited and if neighbour != parent then there is a cycle
# do not forget to propagate the return value to the top . 

#adjacency matrix
def dfs(graph,node,visited,parent,V):
    visited[node] = True
    for neighbour in range(V):
        if graph[node][neighbour] == 1:
            if visited[neighbour]==0:
                if dfs(graph,neighbour,visited, node, V):#----**** important to propagate cycle detection result upward
                    return True
            elif neighbour!=parent:
                return True
    return False 
    
def cycleDetectDfs(graph):
    V = len(graph)#no. of vertices
    visited = [0]*V
    for node in range(V):
        if not visited[node]:
            if(dfs(graph,node,visited,-1,V)):
                return True
    return False



#adjacency list
def dfsList(graph,node,visited,parent):
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfsList(graph,neighbour,visited,node):
                return True
        elif neighbour!=parent:
            return True
    return False

def cycleDetectDfslist(graph):
    V = len(graph)
    visited = set()
    for node in range(V):
        if node not in visited:
            if dfsList(graph,node,visited,-1):
                return True
    return False