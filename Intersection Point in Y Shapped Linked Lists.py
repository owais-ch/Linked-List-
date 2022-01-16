'''Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.'''

def intersetPoint(head1,head2):
    n=head1
    
    dict1=dict()
    
    while n!=None:
        dict1[n]=1
        n=n.next
        
    m=head2
    
    while m!=None:
        if m in dict1:
            return m.data
        else:
            pass
        m=m.next
        
    return -1
