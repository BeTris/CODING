class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def deleteFromFirst(head):
    curr = head
    head = head.next
    curr.next = None #no need to free as automatic garbage collector
    return head

def deleteFromLast(head):
    if head == None:
        return None
    curr = head
    if curr.next == None:
        #only 1 node
        return None
    while(curr.next.next!=None):
        curr = curr.next
    curr.next = None
    return head

def deleteFromPos(head,pos):
    if head == None:
        return None
    
    pass

def deleteValue(head,val):
    pass

def printLL(head):
    while(head!=None):
        print(head.data,end="->")
        head=head.next
    print("None")

def arr2ll(arr):
    head = Node(arr[0])
    temp = head
    for item in arr[1:]:
        temp.next = Node(item)
        temp = temp.next
    return head

head = arr2ll([1,2,3])
# head1 = deleteFromFirst(head)
# head2 = deleteFromLast(head)
# printLL(head1)
# printLL(head2)