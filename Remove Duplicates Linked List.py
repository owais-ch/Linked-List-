'''

Given a singly-linked list of integers sorted in increasing order, remove duplicates from it by traversing the list only once.

Input: 1 —> 2 —> 2 —> 2 —> 3 —> 4 —> 4 —> 5 —> None
Output: 1 —> 2 —> 3 —> 4 —> 5 —> None

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def removeDuplicates(self, head: Node) -> Node:
		n=head
		m=head
		
		if n==None:
			return None
		
		head2=m
		
		while n.next!=None:
			if n.next.data!=m.data:
				m.next=n.next
				m=m.next
				
			n=n.next
			if n==None:
				break
		m.next=None	
		return head2
