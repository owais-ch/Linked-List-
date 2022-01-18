'''Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.
If there are even nodes, then there would be two middle nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it 
should be modified to 1->2->3->5->6.
If the input linked list is NULL or has 1 node, then it should return NULL

Example 1:

Input:
LinkedList: 1->2->3->4->5
Output: 1 2 4 5'''


from math import ceil

def deleteMid(head):
    n=head
    
    count=0
    
    while n!=None:
        count+=1
        n=n.next
    if count%2!=0:    
        index=ceil(count/2)-2
    else:
        index=ceil(count/2)-1
    
    m=head
    head=m
    
    i=0
    
    while index!=i:
        m=m.next
        i+=1
        
    m.next=m.next.next
    return head
