'''Given a singly linked list, the task is to rearrange it in a way that all odd position nodes are together and all even positions node are together.
Assume the first element to be at position 1 followed by second element at position 2 and so on.
Note: You should place all odd positioned nodes first and then the even positioned ones. (considering 1 based indexing). Also, the relative order of odd positioned nodes and even positioned nodes should be maintained.

Example 1:

Input:
LinkedList: 1->2->3->4
Output: 1 3 2 4 '''


class Solution:    
    def rearrangeEvenOdd(self, head):
        n=head
        m=n.next
        
        head1=n
        head2=m
        
        while n!=None or m!=None:
            if n.next==None or m.next==None:
                break
            n.next=n.next.next
            m.next=m.next.next
            n=n.next
            m=m.next
            
        n.next=head2
        if m!=None:
            m.next=None
        
        return head1
