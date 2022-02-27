'''Given a Cirular Linked List of size N, split it into two halves circular lists. If there are odd number of nodes in the given circular linked list then out 
of the resulting two halved lists, first list should have one node more than the second list. The resultant lists should also be circular lists and not linear lists.

Example 1:

Input:
Circular LinkedList: 1->5->7
Output:
1 5
7'''

from math import ceil

class Solution:
    def splitList(self, head, head1, head2):
        n=head
        list1=[head]
        
        while n.next!=head:
            list1.append(n.next)
            n=n.next
            
        length=len(list1)
        
        length1=ceil(length/2)
        length2=length-length1
        
        m=list1[0]
        head1=m
        
        for i in range(1,length1):
            hh=list1[i]
            m.next=hh
            m=m.next
            
        m.next=head1
        
        q=list1[length1]
        head2=q
        
        for i in range(length1+1,length):
            gg=list1[i]
            q.next=gg
            q=q.next
        if length2==1:
            q.next=None
        q.next=head2
        
        return head1,head2
