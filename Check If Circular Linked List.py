'''Given head, the head of a singly linked list, find if the linked list is circular or not. A linked list is called circular if it not NULL terminated
and all nodes are connected in the form of a cycle. An empty linked list is considered as circular.

Note: The linked list does not contains any inner loop.

Example 1:

Input:
LinkedList: 1->2->3->4->5
(the first and last node is connected,
i.e. 5 --> 1)
Output: 1'''

def isCircular(head):
    n=head.next
    
    while n!=None:
        if n.next==head:
            return 1
        n=n.next    
    return 0
