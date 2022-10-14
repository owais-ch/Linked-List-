'''Given a sorted doubly linked list and a value to insert, write a function to insert the value in sorted way.
Initial doubly linked list'''

def insert_sort(head,x):
    n=head
    head=n
    if n.data>x:
        m=Node(x)
        m.next=head
        head.prev=m
        head=m
        return head
    
    while n.next.next!=None:
        if n.data<x and n.next.data>=x:
            m=Node(x)
            m.next=n.next
            n.next=m
            m.prev=n
            n.next.prev=m
            return head
        n=n.next
        
    m=Node(x)
    m.next=n.next
    n.next=m
    m.prev=n
    
    return head
