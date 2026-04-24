class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def arr2ll(arr):
    head = Node(arr[0])
    temp = head
    for item in arr[1:]:
        temp.next = Node(item)
        temp = temp.next
    return head

def printList(head):
    while head != None:
        print(head.data,end = "->")
        head = head.next
    print("None")

head = arr2ll([1,2,3,4])
printList(head)