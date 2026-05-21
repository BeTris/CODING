class Solution:
    def rotateMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        #first transpose
        for row in range(0,m):
            for col in range(row+1,n):
                matrix[row][col],matrix[col][row]=matrix[col][row],matrix[row][col]
        #then reverse each row
        for row in range(0,m):
            for col in range(0,n//2):
                matrix[row][col],matrix[row][n-1-col] =matrix[row][n-1-col],matrix[row][col]
        return matrix
'''Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.



The rotation must be done in place, meaning the input 2D matrix must be modified directly.


Example 1

Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



Output: matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]



Example 2

Input: matrix = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]



Output: matrix = [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]

'''