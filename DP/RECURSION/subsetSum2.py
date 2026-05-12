#arr can have duplicates but answer cannot have duplicate subsets
#return all unique subsets
def subsetSum2(arr,ind,val,res):
    if ind == len(arr):
        res.append(val.copy())
        return res
    for i in range(ind,len(arr)):
        if (i>ind and arr[i]==arr[i-1]):
            continue
        val.append(arr[i])
        subsetSum2(arr,i+1,val,res)
        val.pop()
    subsetSum2(arr,i+1,val,res)
    return res
print(subsetSum2([1,2,2],0,[],[]))

def subsetSum2Striver(arr,ind,val,res):
    res.append(val.copy())
    for i in range(ind,len(arr)):
        if (i>ind and arr[i]==arr[i-1]):
            continue
        val.append(arr[i])
        subsetSum2Striver(arr,i+1,val,res)
        val.pop()
    # subsetSum2Striver(arr,i+1,val,res)
    return res
print(subsetSum2Striver([1,2,2],0,[],[]))