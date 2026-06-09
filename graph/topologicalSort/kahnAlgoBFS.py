#kahn's algorithm
#instead of visited keep inorder array 
#append which ever nodes have inorder as 0 to queue
#pop from queue , and decrease inorder by 1 for each node which had an edge to the node
def kahnAlgo(adjList):
    V = len(adjList)
    queue = []
    res = []
    inOrder = [0]*V
    for i in range(V):
        values = adjList[i]
        for value in values:
            inOrder[value]+=1
    # print(inOrder)
    for i in range(V):
        if inOrder[i]==0:
            queue.append(i)
    #starting queue is created now
    while(queue):
        val = queue.pop(0)
        res.append(val)
        for item in adjList[val]:
            inOrder[item] -= 1
            if inOrder[item] == 0:
                queue.append(item)
    return res
    

kahnAlgo([[1],[2],[3,4],[6],[5],[3],[],[1,9],[7],[]])
