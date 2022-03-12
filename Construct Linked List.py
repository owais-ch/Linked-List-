'''

Given an array of integers, implement a linked list out of the array keys. The solution should create a new node for every key and insert it onto the list's front.

Input : [1, 2, 3, 4, 5]
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

	def construct(self, keys: List[int]) -> Node:
		n=Node(keys[0])
		head=n
		length=len(keys)
		
		for i in range(1,length):
			hh=Node(keys[i])
			n.next=hh
			n=n.next
			
		return head
