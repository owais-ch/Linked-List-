'''
Given a sorted doubly linked list and an element X, your need to insert the element X into correct position in the sorted DLL.

Example 1: 3->5->8>10->12

x=9

1->3->5->8->9->10->12
'''

def sortedInsert(head, x):
    n=head
    
    temp=-9999
    
    if x<=n.data:
        m=Node(x)
        m.next=head
        head.prev=m
        head=m
        return head
        
    while n!=None and n.data<=x:
        temp=n
        n=n.next
        
    m=Node(x)
    
    if n==None:
        m.next=temp.next
        temp.next=m
        m.prev=temp
        return head
    m.next=temp.next
    temp.next=m
    n.prev=m
    m.prev=temp
    
    return head
