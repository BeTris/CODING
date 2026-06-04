#level order traversal
from collections import deque
def levelOrder(graph,startNode):
    visited = set([startNode])
    queue = deque([startNode])
    level = []
    l = [startNode]
    n = len(graph)
    while(queue):
        node = queue.popleft()
        if l!=[]:
            level.append(l)
        l = []
        for neighbour in range(n):
            if neighbour not in visited and graph[node][neighbour]==1:
                queue.append(neighbour)
                l.append(neighbour)
                visited.add(neighbour)
    return level
    
graph = [
    [0, 1, 1, 0, 0, 0],  # 0 → 1, 2
    [1, 0, 0, 1, 1, 0],  # 1 → 0, 3, 4
    [1, 0, 0, 0, 0, 1],  # 2 → 0, 5
    [0, 1, 0, 0, 0, 0],  # 3 → 1
    [0, 1, 0, 0, 0, 1],  # 4 → 1, 5
    [0, 0, 1, 0, 1, 0],  # 5 → 2, 4
]

print(levelOrder(graph,0))