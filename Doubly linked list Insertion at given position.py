'''
Given a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at the position just after pth node in the doubly linked list.

Example 1:

Input:
LinkedList: 2<->4<->5
p = 2, x = 6 
Output: 2 4 5 6
Explanation: p = 2, and x = 6. So, 6 is
inserted after p, i.e, at position 3
(0-based indexing).
'''
def addNode(head, p, data):
    n=head
   
    i=0
   
    while n!=None and i<p:
        n=n.next
        i+=1
    
    m=Node(data)
    if n.next==None:
        m.next=n.next
        n.next=m
        m.prev=n
    else:
        temp=n.next
        m.next=n.next
        n.next=m
        temp.prev=m
        m.prev=n
    
    return head
