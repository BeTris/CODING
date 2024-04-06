#!!!!!!!!!! 3 ways of working with patterns in recursion!!!!!!!!!!!#

# getAllPattern() : How to get all patterns which match
# getOnePattern() : How to use boollean to get only one pattern
# getCountOfPatterns() : How to use integers to count number of patterns

#Func to print all subsequences whose sum are equal to 2.If no such exists return -1
def getAllPattern(arr,temp_sum,sum,index,n,temp_arr):
    #print(temp_arr,temp_sum,index)
    if(index>=n):
        if temp_sum!=sum:
            return -1
        else:
            print(temp_arr)
            return
    temp_arr.append(arr[index])
    getAllPattern(arr,temp_sum+arr[index],sum,index+1,n,temp_arr)
    temp_arr.pop()
    #temp_sum = temp_sum-arr[index]
    getAllPattern(arr,temp_sum,sum,index+1,n,temp_arr)



#Func to print only one subsequence whose sum is equal to 2. If no such exists return -1. Don't use global variable. Use functional method.
def getOnePattern(arr,temp_sum,sum,index,n,temp_arr):
    if(index>=n):
        if temp_sum!=sum:
            return -1
        else:
            print(temp_arr)
            return True
    temp_arr.append(arr[index])
    if(getOnePattern(arr,temp_sum+arr[index],sum,index+1,n,temp_arr)==True):
        return True
    temp_arr.pop()
    #temp_sum = temp_sum-arr[index]
    if(getOnePattern(arr,temp_sum,sum,index+1,n,temp_arr)==True):
        return True
    return False

#Func to count the number of patterns whose sum is equal to given SUM 
def getCountOfPatterns(arr,temp_sum,sum,index,n):
    if(index>=n):
        if temp_sum!=sum:
            return -1
        else:
            print(temp_arr)
            return True
    temp_arr.append(arr[index])
    if(getOnePattern(arr,temp_sum+arr[index],sum,index+1,n,temp_arr)==True):
        return True
    temp_arr.pop()
    #temp_sum = temp_sum-arr[index]
    if(getOnePattern(arr,temp_sum,sum,index+1,n,temp_arr)==True):
        return True
    return False



arr = [1,2,1,3,-1]
n = len(arr)
res_sum = 2
temp_sum = 0
index = 0
print("run getAllPattern")
getAllPattern(arr,temp_sum,res_sum,index,n,[])
print("run getOnePattern")
getOnePattern(arr,temp_sum,res_sum,index,n,[])
print("run getCountOfPatterns")
getCountOfPatterns(arr,temp_sum,res_sum,index,n)