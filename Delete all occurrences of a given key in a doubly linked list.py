'''Given a doubly linked list and a key x. The problem is to delete all occurrences of the given key x from the doubly linked list.'''

def delete_all(head,x):
    n=head
    
    m=None
    headm=None
    
    while n!=None:
        if n.data!=x:
            if m==None:
                m=n
                headm=m
                temp=m
            else:
                m.next=n
                m=m.next
                m.prev=temp
                temp=m
        n=n.next
    m.next=None    
    return headm
