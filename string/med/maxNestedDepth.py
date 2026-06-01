'''A string s is a valid parentheses string (VPS) if it meets the following conditions:

It only contains digits 0-9, arithmetic operators +, -, *, /, and parentheses (, ).
The parentheses are balanced and correctly nested.


Your task is to compute the maximum nesting depth of parentheses in s. The nesting depth is the highest number of parentheses that are open at the same time at any point in the string.


Example 1

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation: The deepest nested sub-expression is ((8)/4), which has 3 layers of parentheses.



Example 2

Input: s = "(1)+((2))+(((3)))"

Output: 3

Explanation: The digit '3' is enclosed in 3 pairs of parentheses.'''
#TC - O(n)
#SC - O(1)
def findMaxDepth(s):
        # Your code goes here
        depth = 0
        max_depth = 0
        for ch in s:
            if ch == "(":
                depth += 1
                max_depth = max(max_depth,depth)
            elif ch == ")":
                depth -= 1#we won't calculate max_Depth here as ((( would return 0 then but correct answer is 3. but this won't happen as we are expecting only valid parenthesis string 
        return max_depth
    
print(findMaxDepth("(1+(2*3)+((8)/4)+1)"))