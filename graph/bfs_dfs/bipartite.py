class Solution:
    def dfs(self,graph,visited,node,color):
        print(visited,node)
        visited[node]=color
        for neighbour in graph[node]:
            print(neighbour,visited)
            if visited[neighbour] == 0:
                if(self.dfs(graph,visited,neighbour,color*-1)==False):#be mindful of propagating the return here
                    return False
            elif visited[neighbour] and visited[neighbour] == color:
                return False
        return True
        
    def isBipartite(self, graph) -> bool:
        V = len(graph)
        visited = [0]*V
        color = 1
        #let there be 2 colors 1 and -1
        for node in range(V):
            if visited[node]==0:
                if not self.dfs(graph,visited,node,color): #be mindful of propagating the return . 
                    return False
        return True
