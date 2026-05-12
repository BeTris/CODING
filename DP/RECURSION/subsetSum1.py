#print a list of sum of all subsets 
def subsetSum1(arr,i,tempSum,res):
    if i == len(arr):
        return res.append(tempSum)
    subsetSum1(arr,i+1,tempSum+arr[i],res)
    subsetSum1(arr,i+1,tempSum,res)
    return res
print(subsetSum1([1,2,3],0,0,[]))
    