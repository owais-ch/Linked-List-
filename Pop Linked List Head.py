'''

Given a singly-linked list of integers, delete its head node, and advance the head pointer to point at the next node in line.

Input : 1 -> 2 —> 3 —> 4 —> None
Output: 2 —> 3 —> 4 —> None

Input : 1 —> None
Output: None

Input : None
Output: None

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def pop(self, head: Node) -> Node:
		if head==None:
			return None
		head=head.next
		
		return head
