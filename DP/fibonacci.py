#f(n) = f(n-1) + f(n-2)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

#memoization TOP - DOWN
#TC = O(N)
#SC = O(N)  RECURSION STACK + O(N) ARRAY 
#0 , 1 , 1 , 2 , 3 , 5
print(fib(5))
def fib_memo(n,dp):
    if (n<=1):
        return n #no  dp[n] = required in base case as it doesn't start new recursion tree 
    if dp[n]==-1:
        #return dp[n] 
        dp[n] = fib_memo(n-1,dp)+fib_memo(n-2,dp)
    return dp[n]
print(fib_memo(5,[-1]*6))

#TABULATION 
#BOTTOM - UP
#step 1 Same array as memoization
#step 2 save base case in array
#recursion starts from n=2 so for loop starts from step 2 also 

def fib_tab(n):
    dp = [0]*(n+1)
    dp[0] = 0 
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(fib_tab(5))

#SPACE-OPTI
def fib_tab_space_optim(n):
    prev = 1
    prev2 = 0
    for i in range(2,n+1):
        i = prev+prev2
        prev2 = prev
        prev = i
    return(prev)

print(fib_tab_space_optim(5))
        