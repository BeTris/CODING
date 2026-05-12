#greedy wont work as we dont know at every point if we select best then it will give optimal or not
#so best way is to select recursiona nd find best way then
#find path with min energy 

#how to write recursion 
#write in index format
#do all stuff on that index
#take min of all stuff
import math
def frog_jump(n,distance):
    if n == 0 :
        return n
    left = frog_jump(n-1,distance) + abs(distance[n]-distance[n-1])
    right =  math.inf
    if n > 1:
        right = frog_jump(n-2,distance) +abs(distance[n]-distance[n-2])
    return min(left,right)
    
print(frog_jump(3,[10,20,30,10]))
print(frog_jump(2,[10,50,10]))

def frog_jump_memo(n,distance,dp):
    if n == 0 :
        return n
    if dp[n]==-1:
        left = frog_jump(n-1,distance) + abs(distance[n]-distance[n-1])
        right =  math.inf
        if n > 1:
            right = frog_jump(n-2,distance) +abs(distance[n]-distance[n-2])
        dp[n] = min(left,right)
    return dp[n]
    
print(frog_jump_memo(3,[10,20,30,10],[-1]*4))
print(frog_jump_memo(2,[10,50,10],[-1]*3))

def frog_jump_tab(n,distance):
    dp = [-1]*(n+1)
    dp[0] = 0
    dp[1] = distance[0]
    for i in range(2,n+1):
        left = dp[i-1]+abs(distance[i]-distance[i-1])
        right = dp[i-2]+abs(distance[i]-distance[i-2])
        # print(dp)
        dp[i] = min(left,right)
    return dp[n]
print(frog_jump_tab(3,[10,20,30,10]))
print(frog_jump_tab(2,[10,50,10]))

def frog_jump_space_optim(n,distance):
    prev2 = 0 
    prev = distance[0]
    for i in range(2,n+1):
        left = prev + abs(distance[i]-distance[i-1])
        right = prev2 +abs(distance[i]-distance[i-2])
        i = min(left,right)
        prev2 = prev
        prev = i
    return prev
print(frog_jump_space_optim(3,[10,20,30,10]))
print(frog_jump_space_optim(2,[10,50,10]))