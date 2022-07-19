'''Given two linked lists sorted in increasing order. Merge them such a way that the result list is in decreasing order (reverse order).

Examples: 

Input:  a: 5->10->15->40
        b: 2->3->20 
Output: res: 40->20->15->10->5->3->2

Input:  a: NULL
        b: 2->3->20 
Output: res: 20->3->2'''

def merge_sorted(head1,head2):
    prev=None
    curr=head1
    next1=None
    
    while curr!=None:
        next1=curr.next
        curr.next=prev
        prev=curr
        curr=next1
        
    first_head=prev
    
    prev=None
    curr=head2
    next1=None
    
    while curr!=None:
        next1=curr.next
        curr.next=prev
        prev=curr
        curr=next1
        
    second_head=prev
    
    n=first_head
    m=second_head
    
    if n.data>=m.data:
        q=n
        head_last=q
        n=n.next
    else:
        q=m
        head_last=q
        m=m.next
        
    while n!=None and m!=None:
        if n.data>=m.data:
            q.next=n
            q=q.next
            n=n.next
        else:
            q.next=m
            q=q.next
            m=m.next
            
    if n!=None:
        q.next=n
        q=q.next
    elif m!=None:
        q.next=m
        q=q.next
        
    return head_last
