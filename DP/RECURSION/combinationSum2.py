#return only unique , arr can have duplicates, can't take one number more than one
def combinationSum2(arr,target,i,combinationList,value):
    if i==len(arr):
        if target == 0:
            return combinationList.add(tuple(value))
        return combinationList
    if arr[i]<=target:
        value.append(arr[i])
        combinationSum2(arr,target-arr[i],i+1,combinationList,value)
        value.pop()
    combinationSum2(arr,target,i+1,combinationList,value)   
    return [list(x) for x in combinationList]

# print(combinationSum2([1,1,1,2,2],4,0,set(),[]))
# print(combinationSum([1,1,1,2,2],4,0,[],[]))
#we cannot add list to set , we need to convert to tuple then add to list
#we can do by making combinationList a set, so only unique is present. 

#more optimised 
#we get arr in sorted manner
def combinationSum2Opti(arr,target,ind,combinationList,value):
    if ind==len(arr):
        if target == 0:
            combinationList.append(value.copy())
            #return combinationList
        return combinationList
    for i in range(ind,len(arr)-1):
        if i>ind and arr[i]==arr[i-1]:
            continue
        if arr[i]<=target:
            value.append(arr[i])
            combinationSum2Opti(arr,target-arr[i],i+1,combinationList,value)
            value.pop()
            combinationSum2Opti(arr,target,i+1,combinationList,value)
    return combinationList

print(combinationSum2Opti([1,1,1,2,2],4,0,[],[]))
        