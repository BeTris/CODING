def rob(ind,n,house):
    if ind == 0:
        return house[ind]
    elif ind < 0 :
        return 0
    pick = house[ind] + rob(ind-2,n,house)
    notPick = 0 + rob(ind-1,n,house)
    return max(pick,notPick)

house = [2,7,9,3,1]
print(rob(len(house)-1,len(house),house))

def rob_memo(ind,n,house,dp):
    if ind == 0:
        return house[ind]
    elif ind < 0 :
        return 0
    pick = house[ind] + rob(ind-2,n,house)
    notPick = 0 + rob(ind-1,n,house)
    if dp[ind] != -1:
        return dp[ind]
    else:
        dp[ind] = max(pick,notPick)
    return dp[ind]

print(rob_memo(len(house)-1,len(house),house,[-1]*(len(house)+1)))

def rob_tab(n,house):
    dp = [-1]*(n+1)
    dp[0] = house[0]
    dp[1] = max(dp[0],house[1])
    for i in range(2,n+1):
        
    pass