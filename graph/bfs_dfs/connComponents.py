from collections import defaultdict
def countComponents(graph,startNode,visited=None):
    if visited == None:
        visited = set()
    n = len(graph)
    count = 0
    def dfs(node):
        for i in range(n):
            if i not in visited and graph[startNode][i] == 1:
                # count +=1
                
                visited.add(i)
                countComponents(graph,i,visited)
    for i in range(n):
        if i not in visited:
            count += 1
            dfs(i)
    return count
    

    
V = 7
edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
#convert this to adj graph or adj matrix

# graph = defaultdict(list)
# for item in edges:
#     graph[item[0]].append(item[1])
#     graph[item[1]].append(item[0])
# print(graph)

# matrix = [[0]*V]*V
# print(matrix)
# for item in edges:
#     matrix[item[0]][item[1]] = 1
#     matrix[item[1]][item[0]] = 1
# print(matrix)


matrix = [[0]*V for _ in range(V)]
for item in edges:
    matrix[item[0]][item[1]] = 1
    matrix[item[1]][item[0]] = 1
print(matrix)
# print(countComponents(graph,0))
print(countComponents(matrix,0))