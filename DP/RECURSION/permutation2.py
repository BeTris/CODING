def permutation2(arr,ind,res):
    if(ind == len(arr)):
        res.append(arr.copy())
        return res
    for i in range(ind,len(arr)):
        arr[ind],arr[i]=arr[i],arr[ind]
        permutation2(arr,ind+1,res)
        arr[ind],arr[i]=arr[i],arr[ind]
    return res
print(permutation2([1,2,3],0,[]))
        