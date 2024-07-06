'''
Is The Doubly Linked List Circular (GFG)

Given a doubly linked list, the task is to check if it is circular or not.

Example 1:

Input:
LinkedList: 2<->3<->4<->5<->6
Output: 0
'''

class Solution: 
    def isCircular(self, head):
        n=head
        
        while n!=None and n.next!=head:
            n=n.next
            
        if n==None:
            return False
            
        return True
