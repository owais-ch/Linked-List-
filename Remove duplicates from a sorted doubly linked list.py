'''Given a sorted doubly linked list containing n nodes. The problem is removing duplicate nodes from the given list.'''

def remove_duplicate(head):
    n=head
    m=head
    headm=m
    temp=m
    while n.next!=None:
        if n.data!=n.next.data:
            m.next=n.next
            m=m.next
            m.prev=temp
            temp=m
        
        n=n.next
        
    m.next=None
    return headm
