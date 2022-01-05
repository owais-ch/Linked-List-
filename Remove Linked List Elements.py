'''Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]'''

class Solution:
    def removeElements(self, head, val):
        if head==None:
            return None
        n=head
        while n!=None:
            if n.val==val:
                n=n.next
                head=n
                
            else:
                break
        if head==None:
            return n
        n=head
        head=n
        m=n.next
        
        while m!=None:
            if m.val==val:
                n.next=m.next
                m=m.next
            else:
                n=n.next
                m=m.next
            
        return head
