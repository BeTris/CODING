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

def reversell(head):
    if head == None:
        return None
    prev  = None
    curr = head
    next = head.next
    while(True):
        curr.next = prev
        prev= curr
        curr=next
        if next == None:
            break
        next = next.next
    return prev

def reversell_recursive(head):
    # Base case: empty list or single node
    if head == None or head.next == None:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reversell_recursive(head.next)
    
    # The node after head is now the last node of the reversed sublist.
    # Make it point back to head.
    head.next.next = head
    
    # head is now the last node, so its next should be None
    head.next = None
    
    return new_head #because we want to return the new_head of reversed linked list



head = arr2ll([1,2,3,4,5])
# head1 = reversell(head)
head2 = reversell_recursive(head)
# printll(head1)
printll(head2)
        