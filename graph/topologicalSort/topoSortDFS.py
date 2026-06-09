#DFS
def dfs(graph,visited,node,stack):
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph,visited,neighbour,stack)
    stack.append(node)
    return stack
def topo(graphList):
    V = len(graphList)
    visited = set()
    stack = []
    for node in range(V):
        if node not in visited:
            res = dfs(graphList,visited,node,stack)
    return stack[::-1]

print(topo([ [ ], [ ], [3], [1], [0,1], [0,2] ]))

#[5,4,2,3,1,0]