# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    p1 = head1
    
    while p1:
        p2 = head2
        while p2:
            if p1 == p2:
                return p1.data
            p2 = p2.next
        p1 = p1.next