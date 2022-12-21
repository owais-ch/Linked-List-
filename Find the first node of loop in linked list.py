'''
Given a linked list of N nodes  Find the first node of loop if the linked list has a loop.

Example 1:

Input:

Output: 3
Explanation:
We can see that there exists a loop 
in the given linked list and the first
node of the loop is 3.
'''
class Solution:
    #Function to find first node if the linked list has a loop.
    def findFirstNode(self, head):
        slow=head
        fast=head
        
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
            
            
        if fast==None or fast.next==None:
            return -1
            
        n=head
        m=slow
        
        while n!=m:
            n=n.next
            m=m.next
            
        return m.data
