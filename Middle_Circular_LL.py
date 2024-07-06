'''
Find Middle of Circular Doubly Linked List (GFG)

Given a circular doubly linked list of odd size n, the task is to print the middle element.
The tail of a circular doubly linked list is connected to head via its next pointer, and the previous pointer of head is connected to the tail.

Example 1:

Input:
LinkedList: 1<-->2<-->3
(The first and the last node is connected,
i.e 3 <--> 1)
Output: 2
'''

class Solution:
    def findMiddle(self, head):
        n=head
        
        length=1
        
        while n.next!=head:
            n=n.next
            length+=1
            
        mid=length//2
        
        i=0
        
        n=head
        
        while i<mid:
            n=n.next
            i+=1
            
        return n.data
