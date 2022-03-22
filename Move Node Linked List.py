'''

Given two singly-linked lists of integers, move front node of the second list in front of the first list. The solution should return a tuple of the first list and the second list.

Input:

X: 1 —> 2 —> 3 —> None
Y: 4 —> 5 —> 6 —> None

Output: (4 —> 1 —> 2 —> 3 —> None, 5 —> 6 —> None)

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def moveNode(self, X: Node, Y: Node) -> Tuple[Node]:
		n=Y
		
		if Y==None:
			return (X,Y)
		head2=Y.next
		
		n.next=X
		head1=n
		
		return (head1,head2)
