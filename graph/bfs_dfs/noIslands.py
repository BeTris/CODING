'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.'''

class Solution:
    def dfs(self,grid,visited,i,j,n,m):
        if(i<0 or i>=n or j<0 or j>=m or grid[i][j]!="1" or visited[i][j]):
            return
        visited[i][j]=1
        self.dfs(grid,visited,i+1,j,n,m)
        self.dfs(grid,visited,i-1,j,n,m)
        self.dfs(grid,visited,i,j+1,n,m)
        self.dfs(grid,visited,i,j-1,n,m)

    def numIslands(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        visited = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if visited[i][j]==0 and grid[i][j]=="1":
                    count+=1
                    self.dfs(grid,visited,i,j,n,m)
        return count