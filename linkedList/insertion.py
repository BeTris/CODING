class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def insertAtHead(head,val):
    if head == None:
        return None
    curr = Node(val)
    curr.next = head
    return curr

def insertAtPos(head,val,pos):
    new_node = Node(val)
    if head == None:
        return None
    if pos == 0:
        #inset at head
        new_node.next = head
        return new_node
    curr = head
    count = 1
    while(curr!=None and count<pos):
        curr= curr.next
        count += 1
    new_node.next = curr.next
    curr.next = new_node
    return head


def insertAtEnd(head,val):
    if head == None:
        return head
    curr = head
    while(curr.next!=None): 
        curr = curr.next
    curr.next = Node(val)
    return head

def insertAtValue(head,data,value):
    if head == None:
        return None
    curr = head
    while(curr.next!=None):
        if curr.next.val == value:
            node = Node(data)
            node = curr.next
            curr.next = node
        curr = curr.next
    return head

def printList(head):
    while head != None:
        print(head.data,end = "->")
        head = head.next
    print("None")

def arr2ll(arr):
    head = Node(arr[0])
    temp = head
    for item in arr[1:]:
        temp.next = Node(item)
        temp = temp.next
    return head

head = arr2ll([1,2,3])
# head1 = insertAtHead(head,5)
# head2 = insertAtPos(head,5,3)
# head3 = insertAtEnd(head,5)
# head4 = insertAtValue(head,5,3)
# printList(head1)
# printList(head2)
# printList(head3)
# printList(head4)