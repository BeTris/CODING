def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while(i<j):
        while(arr[i]<pivot and i<=high-1):
            i+=1
        while(arr[j]>pivot and j>=low):
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
        
        


def quickSort(arr,l,r):
    if(l<r):
        pivotIndex = partition(arr,l,r)
        quickSort(arr,l,pivotIndex)
        quickSort(arr,pivotIndex+1,r)
    return


arr = [12, 11, 13, 5, 6, 7]
print("Given array is:", arr)

quickSort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)
