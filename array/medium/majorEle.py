'''Given an integer array nums of size n, return the majority element of the array.



The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.


Example 1

Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

Output: 7

Explanation:

The number 7 appears 5 times in the 9 sized array

Example 2

Input: nums = [1, 1, 1, 2, 1, 2]

Output: 1

Explanation:

The number 1 appears 4 times in the 6 sized array'''

class Solution:
    def majorityElement(self, nums):
        ele = nums[0]
        cnt = 1
        for i in range(1,len(nums)):
            if cnt ==0:
                ele = nums[i]
                cnt += 1 
            elif nums[i]==ele:
                cnt += 1
            else:
                cnt
                cnt -=1
        return ele