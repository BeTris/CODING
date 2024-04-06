def getFactorial(n,answer):
    if(n<=1):
        return answer
    answer  =  getFactorial(n-1,answer*n)
    return answer
print(getFactorial(5,1))
