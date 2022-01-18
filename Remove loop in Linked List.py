'''Given a linked list of N nodes such that it may contain a loop.

A loop here means that the last node of the link list is connected to the node at position X. If the link list does not have any loop, X=0.

Remove the loop from the linked list, if it is present.  '''


class Solution:
    def removeLoop(self, head):
        n=head
        head=n
        dict1=dict()
        
        while n!=None:
            dict1[n]=1
            if n.next in dict1:
                n.next=None
                return head  
            n=n.next
            
        return head 
