#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeDuplicates(llist):
    # Write your code here
    p1 = llist.next
    p2 = llist
    
    while p1:
        if p1.data != p2.data:
            p2.next = p1
            p2 = p2.next
        p1 = p1.next
    
    if p2.next:
        p2.next = None
        
    return llist