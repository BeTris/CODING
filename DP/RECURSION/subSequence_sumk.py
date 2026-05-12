def printAllSubSequence(arr=[],i=0,values=[],subSequence=[],tempSum=0,k=3):
    if (i==len(arr)):
        if(tempSum == k):
            subSequence.append(values.copy())
        return
    values.append(arr[i])
    printAllSubSequence(arr,i+1,values,subSequence,tempSum+arr[i],k)
    values.pop()
    printAllSubSequence(arr,i+1,values,subSequence,tempSum,k)
    return subSequence
print(printAllSubSequence([1,2,3],0,[],[],0,0))
            
            
def printIfAnySubSequence(arr,i,tempSum,k):
    if i==len(arr):
        if tempSum == k:
            return True
        return False
    return printIfAnySubSequence(arr,i+1,tempSum+arr[i],k) or printIfAnySubSequence(arr,i+1,tempSum,k)
print(printIfAnySubSequence([0,1,2,3],0,0,0))

def countSubsequenceWithSumK(arr,i,tempSum,k):
    if i == len(arr):
        if tempSum == k:
            return 1
        return 0
    return(countSubsequenceWithSumK(arr,i+1,tempSum+arr[i],k)+countSubsequenceWithSumK(arr,i+1,tempSum,k))

print(countSubsequenceWithSumK([1,2,3],0,0,3))
            