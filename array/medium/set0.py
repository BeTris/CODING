'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0. You must do it in place.


Example 1

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]

Output: [[1,0,1],[0,0,0],[1,0,1]]

Explanation:

Element at position (1,1) is 0, so set entire row 1 and column 1 to 0.

Example 2

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Explanation:

There are two zeroes: (0,0) and (0,3).

Row 0 → all elements become 0
Column 0 '''

class Solution:

    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        #brute force time  -> O(n^2) space -> O(m)+O(n)
        i_list = []
        j_list = []
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    i_list.append(i)
                    j_list.append(j)
        for i in range(0,m):
            for j in range(0,n):
                if i in i_list or j in j_list:
                    matrix[i][j] = 0
        return matrix

        #optimal
        col0 = 1
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]==0:
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j],matrix[i][0]=0,0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j] != 0:
                    if j==0:
                        if col0 == 0:
                            matrix[i][j]=0
                    elif matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        return matrix 