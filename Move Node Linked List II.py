'''

Given a singly-linked list of integers, move its last node to the front.

Input : 1 —> 2 —> 3 —> 4 —> None
Output: 4 —> 1 —> 2 —> 3 —> None

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def moveNode(self, head: Node) -> Node:
		n=head
		if n==None:
			return None
		elif n.next==None:
			return n
		
		list1=[]
		
		while n.next.next!=None:
			n=n.next
			
		m=n.next
		
		n.next=None
		
		m.next=head
		
		return m
