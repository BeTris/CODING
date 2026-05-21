'''Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.



Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in any order.


Example 1

Input: nums = [1, 6, 2, 10, 3], target = 7

Output: [0, 1]

Explanation:

nums[0] + nums[1] = 1 + 6 = 7

Example 2

Input: nums = [1, 3, 5, -7, 6, -3], target = 0

Output: [1, 5]

Explanation:

nums[1] + nums[5] = 3 + (-3) = 0'''

class Solution:
    def twoSum(self, nums, target):
        #solution 1 - using hashmap space and time O(N)
        # hm = {}
        # for i in range(0,len(nums)):
        #     if target-nums[i] in hm.keys():
        #         return [i,hm[target-nums[i]]]
        #     else:
        #         hm[nums[i]] = i
        # return[-1,-1]
        
        #solution 2 : 2 pointer  time O(n), space constant if 
        
        i = 0
        j = len(nums)-1
        mp={}
        for i in range(0,len(nums)):
            mp[nums[i]] = i
        nums = sorted(nums)
        i=0
        while i<j:
            if nums[i]+nums[j]==target:
                return [mp[nums[i]],mp[nums[j]]]
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                i+=1
        return [-1,-1]
