'''

Given a singly-linked list of integers, which may contain a cycle, remove the cycle if present.

Input: 1 → 2 → 3 → 4 ─┐
		   └──────────┘
Output: 1 → 2 → 3 → 4 → None


Input : 1 → 2 → 3 → 4 → None
Output: 1 → 2 → 3 → 4 → None

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def removeCycle(self, head: Node) -> None:
		n=head
		
		if n==None:
			return head
		
		list1=[n]
		
		while n.next!=None:
			if n.next in list1:
				n.next=None
				return head
			n=n.next
			list1.append(n)
			
		return head
