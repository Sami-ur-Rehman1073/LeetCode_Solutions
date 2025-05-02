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

def mergeKLists(lists):
    merged_list = []
    for i in lists:
        current = i
        while current:
            merged_list.append(current.val)
            current = current.next
    merged_list.sort()
    return create_linked_list(merged_list)

print(mergeKLists([create_linked_list([1,4,5]),
                   create_linked_list([1,3,4]),
                   create_linked_list([2,6])]))
    


        
        