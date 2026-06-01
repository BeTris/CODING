#DONE
'''Largest Odd Number in a String

Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.



The number returned should not have leading zero's. But the given input string may have leading zero. (If no odd number is found, then return empty string.)


Example 1

Input : s = "5347"

Output : "5347"

Explanation :

The odd numbers formed by given strings are --> 5, 3, 53, 347, 5347.

So the largest among all the possible odd numbers for given string is 5347.

Example 2

Input : s = "0214638"

Output : "21463"

Explanation :

The different odd numbers that can be formed by the given string are --> 1, 3, 21, 63, 463, 1463, 21463.

We cannot include 021463 as the number contains leading zero.

So largest odd number in given string is 21463.

'''
#__Time Complexity:__ O(n) — ✅ Optimal
#__Space Complexity:__ O(1) extra — ✅ Optimal
#can be done in one pass using lstrip(0)
def longOdd(nums):
    n = len(nums)
    endIndex = -1
    startIndex = -1
    for i in range(n-1,-1,-1):
        if int(nums[i])% 2 == 1:
            endIndex = i
            break
    
    for i in range(0,n,1):
        if nums[i] == '0':
            continue
        startIndex = i 
        break
    if startIndex==-1 and  endIndex == -1:
        return ""
    return nums[startIndex:endIndex+1]

print(longOdd("5347"))
     