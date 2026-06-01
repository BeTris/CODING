#DONE
'''Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.



A shift on s consists of moving the leftmost character of s to the rightmost position.



For example, if s = "abcde", then it will be "bcdea" after one shift.


Example 1

Input : s = "abcde" , goal = "cdeab"

Output : true

Explanation :

After performing 2 shifts we can achieve the goal string from string s.

After first shift the string s is => bcdea

After second shift the string s is => cdeab.

Example 2

Input : s = "abcde" , goal = "adeac"

Output : false

Explanation :

Any number of shift operations cannot convert string s to string goal.'''
#TC - O(n^2)
#SC -> O(n) -> at each iteration temp string created as string is immutable in python
def rotateString(s,goal):
    #max no. of shifts can be len(s)-1
    if s == goal:
        return True
    i = 1
    n = len(s)
    while(i<n):#O(n^2)
        if s[i:n]+s[0:i] == goal: #O(n)
            return True
        i+=1
    return False

print(rotateString("abcde","cdeab"))

def rotateStringOptim(s,goal):
    #max no. of shifts can be len(s)-1
    return True if len(s)==len(goal) and goal in s+s else False

print(rotateStringOptim("abcde","cdeab"))

#To check if string is in another string 
#brute force TC- O(N*M)  SC -O(1)
#KMP[Knuth-Morris-Pratt] O(n+m) SC - O(m)
#python in function which internally uses two way or Boyer-Moore TC- O(n+m) SC - O(1) [Most optimised]