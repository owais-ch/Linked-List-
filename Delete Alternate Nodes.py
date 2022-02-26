'''Given a Singly Linked List of size N, delete all alternate nodes of the list.

Example 1:

Input:
LinkedList: 1->2->3->4->5->6
Output: 1->3->5
Explanation: Deleting alternate nodes
results in the linked list with elements
1->3->5.'''

class Solution: 
    def deleteAlt(self, head):
        n=head
        head=n
        if n.next==None:
            return head
        while n!=None:
            n.next=n.next.next
            n=n.next
            if n==None:
                break
            elif n.next==None:
                break
            
        return head
