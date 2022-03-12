'''

Given an array of integers, construct a linked list out of the array keys. The solution should create a new node for every key and efficiently insert it onto the list's tail.

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
		n=Node(keys[-1])
		count=-2
		for i in range(1,len(keys)):
			hh=Node(keys[count])
			hh.next=n
			n=hh
			count-=1
			
		head=n
		return head
