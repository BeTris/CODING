'''Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.



The sorting must be done in-place, without making a copy of the original array.


Example 1

Input: nums = [1, 0, 2, 1, 0]

Output: [0, 0, 1, 1, 2]

Explanation:

The nums array in sorted order has 2 zeroes, 2 ones and 1 two

Example 2

Input: nums = [0, 0, 1, 1, 1]

Output: [0, 0, 1, 1, 1]

Explanation:

The nums array in sorted order has 2 zeroes, 3 ones and zero twos'''

def sort012(nums):
    ind_0 = 0
    ind_2 = len(nums)-1
    ind = 0
    #0 to ind_0-1 -> all 0
    # ind_0 to ind-1 -> all 1
    # ind to ind_2-1 -> unknown
    # ind_2 to len(nums)-1 -> all 2
    #so unknown is ind to ind_2-1
    while(ind<=ind_2):
        if nums[ind] == 0:
            nums[ind],nums[ind_0] = nums[ind_0],nums[ind]
            ind_0 += 1
            ind += 1
        elif nums[ind] == 1:
            ind+=1
        else:
            nums[ind],nums[ind_2] = nums[ind_2],nums[ind]
            ind_2 -= 1
    return nums

print(sort012([0,2,1,1,0,2,1,0]))