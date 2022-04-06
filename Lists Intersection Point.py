'''

Given two non-empty singly-linked lists, where the tail of the second list points to a node in the first list, return the node where both lists intersect. If the lists does not intersect, return None.

Input:

1 ——⮞ 2 ——⮞ 3 ——⮞ 4 ——⮞ 5 ——⮞ nullptr		// first linked list
				   ⮝
1 ——⮞ 2 ——⮞ 3 ────┘							// second linked list

Output: Node 4

Explanation: The tail of the second list is connected to the fourth node of the first list. The solution should return a pointer to node 4 as the intersection point.

'''

class Solution:
	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def findIntersectionPoint(self, first: Node, second: Node) -> Node:
		list1=[]
		list2=[]
		
		m=first
		
		while m!=None:
			list2.append(m)
			m=m.next
			
		n=second
		
		while n!=None:
			if n in list2:
				return n
			n=n.next
			
