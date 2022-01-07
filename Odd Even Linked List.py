'''Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]'''

class Solution:
    def oddEvenList(self, head):
        n=head
        head=n
        if n==None:
            return None
        elif n.next==None:
            return n
        m=n.next
        q=m
        
        while n!=None or m!=None:
            if n.next==None or m.next==None:
                break
            
            n.next=n.next.next
            m.next=m.next.next
            
            n=n.next
            m=m.next
            
        n.next=q
        
        return head
