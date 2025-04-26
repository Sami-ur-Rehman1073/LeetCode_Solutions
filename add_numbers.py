class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(lst):
    dummy = ListNode()  
    current = dummy

    for i in lst:
        current.next = ListNode(i) 
        current = current.next     

    return dummy.next

def addTwoNumbers(l1, l2):
    int1 = []
    int2 = []
    current1 = l1
    current2 = l2
    if current1:
        int1.append(current1.val)
        current1 = current1.next
    else:
        int1.append(0)
    
    if current2:
        int2.append(current2.val)
        current2 = current2.next
    else:
        int2.append(0)
    temp = ''.join(str(i) for i in int1)  
    x = int(temp[::-1])

    temp = ''.join(str(i) for i in int2)  
    y = int(temp[::-1]) 

    z = str(x + y)

    result = [int(i) for i in z]

    return create_linked_list(result[::-1])


print(addTwoNumbers(create_linked_list([2,4,3]), create_linked_list([5,6,4])))