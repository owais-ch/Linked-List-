'''Given a singly linked list, remove all the nodes which have a greater value on the right side. 

Examples: 
a) The list 12->15->10->11->5->6->2->3->NULL should be changed to 15->11->6->3->NULL. Note that 12, 10, 5 and 2 have been deleted because there is a greater value on the right side. 
When we examine 12, we see that after 12 there is one node with a value greater than 12 (i.e. 15), so we delete 12. 
When we examine 15, we find no node after 15 that has a value greater than 15, so we keep this node. 
When we go like this, we get 15->6->3
b) The list 10->20->30->40->50->60->NULL should be changed to 60->NULL. Note that 10, 20, 30, 40, and 50 have been deleted because they all have a greater value on the right side.
c) The list 60->50->40->30->20->10->NULL should not be changed.'''

def delete_nodes(head):
    prev=None
    curr=head
    next1=None
    
    while curr!=None:
        next1=curr.next
        curr.next=prev
        prev=curr
        curr=next1
        
    head=prev
    
    n=head
    count=0
    q=head
    head1=q
    while n!=None:
        if count==0:
            maximum=n.data
            count+=1
        elif n.data>maximum:
            maximum=n.data
            q.next=n
            q=q.next
            
        n=n.next
    q.next=None
    prev=None
    curr=head1
    next1=None
    
    while curr!=None:
        next1=curr.next
        curr.next=prev
        prev=curr
        curr=next1
        
    return prev
