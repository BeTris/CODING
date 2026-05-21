class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def arr2ll(arr):
    curr = Node(None)
    head = curr
    for item in arr:
        curr.next = Node(item)
        curr = curr.next
    return head.next

def printll(head):
    curr=head
    while(curr!=None):
        print(curr.data,end='->')
        curr = curr.next
    print("None")
    
def addOne(head):
    pass

head = arr2ll([1,2,3,4,5])
head1 = addOne(head)
printll(head1)