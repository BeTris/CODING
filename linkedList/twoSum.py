class Node : 
    def __init__(self,data):
        self.data = data
        self.next = None

def twoSum(head1,head2):
    if head1 == None and head2:
        return None
    curr1 = head1
    curr2 = head2
    carry = 0
    prev  = Node(None)
    curr = Node(carry)
    prev.next = curr
    while(curr1!=None and curr2 != None):
        val = (curr1.data + curr2.data + carry)%10
        carry =  (curr1.data + curr2.data + carry)//10
        curr.data = val
        curr1 = curr1.next
        curr2 = curr2.next
        curr.next = Node(0)
        curr = curr.next
    if curr1!=None:
        while(curr1!=None):
            val = (curr1.data + carry)%10
            carry =  (curr1.data + carry)//10
            curr.data = val
            curr1 = curr1.next
            curr = curr.next
    if curr2!=None:
        while(curr2!=None):
            val = (curr2.data + carry)%10
            carry =  (curr2.data + carry)//10
            curr.data = val
            curr2 = curr2.next
            curr = curr.next
    return prev.next

           
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

head1 = arr2ll([1,2,4])
head2 = arr2ll([4,5,6])
head = twoSum(head1,head2)
printList(head)