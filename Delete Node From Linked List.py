'''Delete a given node from a singly-linked list. You do not have access to the head of the list. Also, the node to be deleted is not the tail of the linked list.

Example 1:
1→2→3→4

Deleting 2nd node, we get

1→3→4'''

class Solution:
	def deleteNode(self, node):
		n=node
		
		while n.next!=None:
			n.data=n.next.data
			if n.next.next==None:
				n.next=None
				break
			n=n.next
