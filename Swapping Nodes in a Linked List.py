'''You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]'''

class Solution:
    def swapNodes(self, head, k):
        n=head
        if n.next==None:
            return n
        length=0
        
        while n!=None:
            length+=1
            n=n.next
        
        if length-k==k-1:
            return head
        n=head
        head=n
        
        for i in range(length):
            if i==k-1:
                mm=n
            elif i==length-k:
                hh=n
            
            n=n.next
            
        mm.val,hh.val=hh.val,mm.val
        
        return head
