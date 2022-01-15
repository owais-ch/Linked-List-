'''Given two lists sorted in increasing order, create a new list representing the intersection of the two lists. The new list should be made with its own memory 
— the original lists should not be changed.
Note: The list elements are not necessarily distinct.

Example 1:

Input:
L1 = 1->2->3->4->6
L2 = 2->4->6->8
Output: 2 4 6
Explanation: For the given first two
linked list, 2, 4 and 6 are the elements
in the intersection.'''

def findIntersection(head1,head2):
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
        
    list3=sorted(list(set(list1).intersection(set(list2))))
    
    length=len(list3)
    
    m=Node(list3[0])
    head=m
    
    for i in range(1,length):
        hh=Node(list3[i])
        m.next=hh
        m=m.next
        
    return head
