'''Given a linked list and a key, remove all occurrences of the key from the Linked List. Return the head of the resultant list.

Example
Linked List: 1→2→3→2→4→7→2
Key: 2
After removal: 1→3→4→7'''

class Solution:
    def removeOccurences(self, head, key):
        n=head

        while n!=None and n.data==key:
            if n.data==key:
                head=n.next
                n=head
				
        if n==None:
            return None
		
        while n.next!=None:
            if n.next.data==key:
                n.next=n.next.next
            else:
                n=n.next
        
        return head  
