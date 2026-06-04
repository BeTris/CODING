#DONE
'''Implement the function myAtoi(s) which converts the given string s to a 32-bit signed integer (similar to the C/C++ atoi function).



Steps to Implement:

First, ignore any leading whitespace characters ' ' until the first non-whitespace character is found.
Check the next character to determine the sign. If it’s a '-', the number should be negative. If it’s a '+', the number should be positive. If neither is found, assume the number is positive.
Read the digits and convert them into a number. Stop reading once a non-digit character is encountered or the end of the string is reached. Leading zeros should be ignored during conversion.
The result should be clamped within the 32-bit signed integer range: [-2147483648, 2147483647]. If the computed number is outside this range, return -2147483648 if the number is less than -2147483648, or return 2147483647 if the number is greater than 2147483647.
Finally, return the computed number after applying all the above steps.

Example 1

Input: s = " -12345"

Output: -12345

Explanation:

Ignore leading whitespaces.
The sign '-' is encountered, indicating the number is negative.
Digits 12345 are read and converted to -12345.
Example 2

Input: s = "4193 with words"

Output: 4193

Explanation:

Read the digits 4193 and stop when encountering the first non-digit character (w).
Constraints

0 ≤ s.length ≤ 200
s consists of English letters (both lowercase and uppercase), Digits '0' to '9', Characters: ' ', '+', '-', and '.'''

def string2Int(s):
    #ignore whitespace,leading 0
    #stop when u get a char or string ends
    #if ourside range then return specific value
    #check for sign
    INT_MIN, INT_MAX = -2147483648, 2147483647
    
    res = 0
    i=0
    #this loop doesn't execute if length is 0
    # if len(s)==0:
    #     return res
    while i < len(s) and s[i] == ' ':
        i += 1
    # else:
    #     return res #only whitespaces
    sign = 1
    if i<len(s) and s[i] == '-':
        sign = -1
        i+=1
    elif  i<len(s) and  s[i] == "+":
        i+=1
    # j = i
    # while(i<len(s) and s[i]==0):    
    # # for j in range (i,len(s)):
    #     # if(s[i] != '0'):
    #     #     break
    #     i+=1
    # else:
    #     return res #only whitespace and then 0 
    # print("jj",j)#s[i].isdigit()
    while(i<len(s) and s[i] in ['0','1','2','3','4','5','6','7','8','9']):
    # for k in range(j,len(s)):
        # if s[i] in ['0','1','2','3','4','5','6','7','8','9']:
        res = res*10+int(s[i])
        if sign * res > INT_MAX:
            return INT_MAX
        if sign * res < INT_MIN:
            return INT_MIN
        # else:
        #     break
        i+=1
    return sign*res

print(string2Int("2147483647425425"))
            