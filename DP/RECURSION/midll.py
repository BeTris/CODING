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


def midll(head):
    if head == None:
        return None
    # if head.next == None:
    #     return head.data
    slow = head
    fast = head
    while(fast!=None and fast.next!=None):
        fast = fast.next.next
        slow = slow.next
    return slow.data

head = arr2ll([1,2,3,4,5,6])
# head1 = reversell(head)
val = midll(head)# printll(head1)
print(val)
        