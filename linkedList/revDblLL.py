class Node:

    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

def reverseDLL(head):
    if head == None:
        return None
    curr = head
    prev = None
    while(curr!=None):
        print(curr.data)
        curr.prev,curr.next = curr.next,curr.prev
        prev = curr
        curr = curr.prev
    return prev

def printLL(head):
    while(head!=None):
        print(head.data,end="->")
        head=head.next
    print("None")

def arr2ll(arr):
    head = Node(arr[0])
    temp = head
    for item in arr[1:]:
        new_node = Node(item)
        temp.next = new_node
        new_node.prev = temp
        temp = temp.next
    return head

head = arr2ll([1,2,3])
head1 = reverseDLL(head)
printLL(head1)