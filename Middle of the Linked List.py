'''Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.'''

class Solution:
    def middleNode(self, head):
        n=head
        
        count=0
        
        while n!=None:
            count+=1
            n=n.next
            
        middle=floor(count/2)
        
        
            
        n=head
        
        for i in range(middle):
            n=n.next
        head=n    
        return head
