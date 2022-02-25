'''Given a doubly linked list and a position. The task is to delete a node from given position in a doubly linked list.

Example 1:

Input:
LinkedList = 1 <--> 3 <--> 4 
x = 3
Output: 1 3  
Explanation: After deleting the node at
position 3 (position starts from 1),
the linked list will be now as 1->3.'''

class Solution:
    def deleteNode(self,head, x):
        if x==1:
            head=head.next
            head.prev=None
            return head
            
        i=1
        n=head
        head=n
        while x-1!=i:
            n=n.next
            i+=1
            
        n.next=n.next.next
        return head
