def merge(arr,l,mid,r):
    k=0
    i=l
    j=mid+1
    temp=[]
    while(i<=mid and j<=r):
        if(arr[i]<arr[j]):
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while(i<=mid):
        temp.append(arr[i])
        i+=1
    while(j<=r):
        temp.append(arr[j])
        j+=1
    for i in range (l,r+1):
        arr[i] = temp[i-l]

def mergeSort(arr,l,r):
    if(l<r):  
        mid = l +(r-l)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)
    return 

arr = [12, 11, 13, 5, 6, 7]
print("Given array is:", arr)

mergeSort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)

