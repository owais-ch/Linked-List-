'''Given a linked list, find the xth node from the end.

Example
Linked list: 1→2→3→4
x: 2
Result: 3'''


class Solution:
	def xthNodeFromEnd(self, head, x):
		n=head
		
		list1=[]
		
		while n!=None:
			list1.append(n)
			n=n.next
			
		return list1[-x]
