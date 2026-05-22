'''
Print the matrix in spiral manner
Subscribe to TUF+

Hints
Company
Given an M * N matrix, print the elements in a clockwise spiral manner.



Return an array with the elements in the order of their appearance when printed in a spiral manner.


Example 1

Input: matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]

Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Explanation:

The elements in the spiral order are 1, 2, 3 -> 6, 9 -> 8, 7 -> 4, 5

Example 2

Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]

Output: [1, 2, 3, 4, 8, 7, 6, 5]

Explanation:

The elements in the spiral order are 1, 2, 3, 4 -> 8, 7, 6, 5

'''
def spiralOrder(matrix):
	m = len(matrix)
	n = len(matrix[0])
	l= 0
	t=0
	r = n-1
	b = m-1
	res = []
	while l <= r and t <= b:
		i = l
		while(i<=r):
			res.append(matrix[t][i])
			i+=1
		t+=1
		i = t
		print(res)
		while(i<=b):
			res.append(matrix[i][r])
			i+=1
		r-=1
		i=r
		print(res)
		while(i>=l and t<=b):#this check if necessary for corner case [[1],[2],[3]]
			res.append(matrix[b][i])
			i-=1
		b-=1
		i=b
		print(res)
		while(i>=t and l<=r): #this check is necessary for corner case [1,2,3]
			res.append(matrix[i][l])
			i-=1
		l+=1
		print(res)
		print(l,r,t,b)
	return res
print(spiralOrder([[1, 2, 3]]))