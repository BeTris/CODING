#return only unique, all distinct in arr, can pickup one number more than once
def combinationSum(arr,target,i,combinationList,value):
    if i==len(arr):
        if target == 0:
            return combinationList.append(value.copy())
        return #combinationList
    if arr[i]<=target:
        value.append(arr[i])
        combinationSum(arr,target-arr[i],i,combinationList,value)
        value.pop()
    combinationSum(arr,target,i+1,combinationList,value)   
    return combinationList

print(combinationSum([2,3,6,7],7,0,[],[]))
# print(combinationSum([1,1,1,2,2],4,0,[],[]))

#TC : (2**n) * k[as we copy from one DS to another]