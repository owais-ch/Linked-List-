'''You are given a circular linked list having N number of nodes, where N is even. You have to split this linked list into two equal-sized circular linked lists.
Here splitting means you have to make two separate circular linked lists, one for the first N/2 nodes and one for the last N/2 nodes.'''

def splitCircularList(head):
    n=head
    
    slow=head
    fast=head
    head1=slow
    
    
    while fast.next!=head and fast.next.next!=head:
        slow=slow.next
        fast=fast.next.next
    temp=slow.next
    
    slow.next=head1
    head2=temp
    m=head2
    
    while m.next!=head:
        m=m.next
    m.next=temp
    m=m.next
    
    return head1,head2
