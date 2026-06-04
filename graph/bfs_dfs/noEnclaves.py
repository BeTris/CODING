'''You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.'''

class Solution:
    #TC:O(n*m)
    #SC:O(n*m)
    def dfs(self,visited,grid,i,j,n,m):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 1 or visited[i][j]==1:
            return
        visited[i][j] = 1
        self.dfs(visited,grid,i+1, j,n,m)
        self.dfs(visited,grid,i-1, j,n,m)
        self.dfs(visited,grid,i, j+1,n,m)
        self.dfs(visited,grid,i, j-1,n,m)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0]*m for _ in range(n)]
        count = 0
        #now do dfs from all 1s on edge
        for i in range(0,n):
            for j in [0,m-1]:
                if visited[i][j]==0 and grid[i][j]==1 :#or i=0 or j=0 or i=n-1 or j=m-1:
                    print(i,j)
                    self.dfs(visited,grid,i,j,n,m)
        for j in range(0,m):
            for i in [0,n-1]:
                if visited[i][j]==0 and grid[i][j]==1 :#or i=0 or j=0 or i=n-1 or j=m-1:
                    self.dfs(visited,grid,i,j,n,m)
        for i in range(0,n):
            for j in range(0,m):
                if visited[i][j]==0 and grid[i][j]==1:
                    count+=1
        return count

                