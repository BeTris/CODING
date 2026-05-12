# #subsequence - continuous / non - contiguous
def printAllSubSequence(arr=[],i=0,values=[],subSequence=[]):
    #print(i,values,subSequence)
    if i==len(arr):
        return subSequence.append(values.copy())
    values.append(arr[i])
    printAllSubSequence(arr,i+1,values,subSequence)
    values.pop()
    printAllSubSequence(arr,i+1,values,subSequence)
    return subSequence
print(printAllSubSequence([1,2,3],0,[],[])) 
print(printAllSubSequence())

#***************IMP CONCEPT of shared lists below********************
# def func(l=[]):
#     l.append(1)
#     print(l)
# func() -> prints[1]
# func() -> prints[1,1]