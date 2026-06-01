#DONE
'''move Outermost Parentheses
A valid parentheses string is defined by the following rules:

It is the empty string "".
If A is a valid parentheses string, then so is "(" + A + ")".
If A and B are valid parentheses strings, then A + B is also valid.


A primitive valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.



Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.



Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.


Example 1

Input: s = "((()))"

Output: "(())"

Explanation:

The input string is a single primitive: "((()))".

Removing the outermost layer yields: "(())".

Example 2

Input: s = "()(()())(())"

Output: "()()()"

Explanation:

Primitive decomposition: "()" + "(()())" + "(())"

After removing outermost parentheses: "" + "()()" + "()"

Final result: "()()()".

Constraints

1 <= s.length <= 10⁵
s[i] is either '(' or ')'
s is a valid parentheses string'''

#TC - O(n^2)
#SC - O(n)
def removeOuterParentheses(s: str) -> str:
    count_o = 0 # count of open ()
    count_c = 0 #count of closed ()
    stack = []
    n = len(s)
    res = []
    for i in range(0,n):
        stack.append(s[i])
        if s[i] == '(':
            count_o += 1
        else:
            count_c += 1
        if count_o == count_c :
            stack.pop()#popping from end is O(1)
            stack.pop(0)#this take O(n) time #list internally works as array so poping has to shift all other char one step 
            res.append(''.join(stack))
            stack = []
    return ''.join(res)
#python lists are dynamic arrays where most appends take O(1) time. 
#if cap is 4 , and list has 3 ele , then appending 4th ele will take constant time, after which when 5th ele is inserted array would automatically resize of 2*n             
#therefore amortized complexity of append is O(1)
# print(removeOuterParentheses("((()))"))
# print(removeOuterParentheses("()(()())(())"))

def optim(s):
    res = ""
    depth = 0
    for ch in s:
        if ch == '(':
            if depth > 0:
                res+=ch
            depth += 1
                
        else:
            depth -= 1
            if depth > 0:
                res+=ch
    return res
print(optim("((()))"))
print(optim("()(()())(())"))