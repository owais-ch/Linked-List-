'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]'''

class Solution:
    def deleteDuplicates(self, head):
        n=head
        m=head
        head1=m
        
        while n!=None:
            if n.data!=m.data:
                m.next=n
                m=m.next
            n=n.next
            
        m.next=None
        
        return head1
