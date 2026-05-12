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
    
#solution1 [ 2 traversals , 3 variabled for count]
#traverse the linked list once and store count of all 0,1,2
#traverse the ll again and keep changing values and decreasing count    
def sortll1(head):
    cnt0,cnt1,cnt2 = 0,0,0
    curr = head
    while(curr!=None):
        if curr.data == 0:
            cnt0 += 1
        elif curr.data == 1 :
            cnt1 += 1
        elif curr.data == 2:
            cnt2 += 1
        else:
            return "invalid"
        curr = curr.next
    curr = head
    while(curr!=None):
        if cnt0 != 0:
            curr.data = 0
            cnt0 -= 1
        elif cnt1 != 0 :
            curr.data = 1
            cnt1 -= 1
        elif cnt2 != 0 :
            curr.data = 2 
            cnt2 -= 1
        curr = curr.next
    return head



#solution2 [no extra space, only extra pointers]
#traverse the linked list once and create 3 separate pointer head , 1 with only 0, 2 with only 1 and 3 with only 2
#at end join all 3
def sortll2(head):
    head0,head1,head2 = Node(-1),Node(-1),Node(-1)
    curr=head
    head0orig = head0
    head1orig=head1
    head2orig=head2
    while curr!=None:
        if curr.data==0:
            head0.next = curr
            head0 = head0.next
        elif curr.data == 1:
            head1.next = curr
            head1 = head1.next
        elif curr.data == 2:
            head2.next = curr
            head2 = head2.next
        curr = curr.next
    head0.next = head1orig.next if head1orig.next else head2orig.next
    head1.next = head2orig.next
    head2.next=None#if we dont do this infinite loop CRITICAL
    return head0orig.next

head = arr2ll([0,2,0,2])
# head1 = sortll1(head)
head2 = sortll2(head)
# printll(head1)
printll(head2)