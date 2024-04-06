def getAllSubsequence(index,arr,sol,n):
    if(index>=n):
        print(sol)
        return
    sol.append(arr[index])
    getAllSubsequence(index+1,arr,sol,n)
    sol.pop()
    getAllSubsequence(index+1,arr,sol,n)    

def main():
    getAllSubsequence(0,[1,2,3],[],3)

if __name__ == "__main__":
    main()
