'''Given two linked lists, your task is to complete the function makeUnion(), that returns the union of two linked lists. This union should include all the distinct elements only.

Example 1:

Input:
L1 = 9->6->4->2->3->8
L2 = 1->2->8->6->2
Output: 1 2 3 4 6 8 9'''

def union(head1,head2):
    n=head1
    
    list1=[]
    
    while n!=None:
        list1.append(n.data)
        n=n.next
        
    m=head2
    
    list2=[]
    
    while m!=None:
        list2.append(m.data)
        m=m.next
        
    list3=sorted(list(set(list1+list2)))
    
    length=len(list3)
    
    q=Node(list3[0])
    head=q
    
    for i in range(1,length):
        hh=Node(list3[i])
        q.next=hh
        q=q.next
        
    return head
