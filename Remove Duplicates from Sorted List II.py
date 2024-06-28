'''Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]'''

from collections import Counter

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
