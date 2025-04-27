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

def mergeTwoLists(list1, list2):
    result = []
    current1 = list1 
    current2 = list2
    while current1:        
        result.append(current1.val)
        current1 = current1.next   

    while current2:
        result.append(current2.val)
        current2 = current2.next

    result.sort()

    return create_linked_list(result)
    


print(mergeTwoLists(create_linked_list([1,2,4]), create_linked_list([1,3,4])))
    