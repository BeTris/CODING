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

def oddevensort(head):
    if head == None or head.next == None:
        return head#or head.next.next == None
    even= head.next
    odd = head
    evenheadorig = even
    #even list is always <= odd list
    while(even!=None and even.next!=None):
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = evenheadorig
    return head

head = arr2ll([1,2,3])
head1 = oddevensort(head)
printll(head1)
        