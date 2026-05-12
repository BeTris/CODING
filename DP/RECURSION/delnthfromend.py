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
    
def delnthFromEnd(head,n): #assuming n <= length of ll
    if head == None or head.next==None:
        return None
    dummy = Node(0)
    dummy.next = head
    fast ,slow = dummy,dummy
    while n != 0: 
        fast = fast.next
        n -= 1
    while(fast.next!=None):
        slow=slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next

head = arr2ll([1,2,3,4,5])
head1 = delnthFromEnd(head,4)
printll(head1)