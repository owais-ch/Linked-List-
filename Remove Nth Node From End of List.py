'''Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]'''

class Solution:
    def removeNthFromEnd(self, head, n):
        m=head
        
        count=0
        
        while m!=None:
            count+=1
            m=m.next
        if count==1:
            head=None
            return None
        m=head
        head=m
        
        i=count-1
        
        while i>n:
            m=m.next
            i=i-1
        if n==count:
            m=m.next
            head=m
        else:
            q=m.next
            m.next=q.next
        
        return head
