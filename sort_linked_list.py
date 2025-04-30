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

def sortList(head):
    nums = []
    current = head
    while current:
        nums.append(current.val)
        current = current.next
    nums.sort()
    return create_linked_list(nums)

print(sortList(create_linked_list([-1,5,3,4,0])))

