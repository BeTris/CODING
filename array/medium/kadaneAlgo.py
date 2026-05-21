'''Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.



A subarray is a contiguous non-empty sequence of elements within an array.


Example 1

Input: nums = [2, 3, 5, -2, 7, -4]

Output: 15

Explanation:

The subarray from index 0 to index 4 has the largest sum = 15

Example 2

Input: nums = [-2, -3, -7, -2, -10, -4]

Output: -2

Explanation:

The element on index 0 or index 3 make up the largest sum when taken as a subarray'''

'''Print subarray with maximum subarray sum (extended version of above problem)'''

#brute force
#O(n^2)
def subArray(nums):
	n = len(nums)
	max_sum = float('-inf')
	for i in range(0,n):
		sum_value = 0
		for j in range(i,n):
			sum_value += nums[j]
			max_sum = max(max_sum,sum_value)
	return max_sum
		
print(subArray([-2, -3, -5, -2, -7, -4]))

#optimal solution using kadane's algo
def subArrayKadane(nums):
    n = len(nums)
    max_sum = float('-inf')
    sum_val = 0
    for i in range(0,len(nums)):
        sum_val += nums[i]
        max_sum = max(max_sum,sum_val)
        if sum_val < 0:
            sum_val = 0
    return max_sum 

print(subArrayKadane([-2, -3, -5, 0, -7, -4]))