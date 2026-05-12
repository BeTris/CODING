#takes extra time
def permutation(arr,ind,val,res,visited):
    if ind == len(arr):
        res.append(val.copy())
        return res
    for i in range(0,len(arr)):
        if(visited[i]==0):
            val.append(arr[i])
            visited[i]=1
            permutation(arr,ind+1,val,res,visited)
            val.pop()
            visited[i]=0
    return res

print(permutation([1,2,3],0,[],[],[0,0,0]))