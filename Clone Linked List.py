'''

Given a singly linked list of integers, return a complete copy of it. The solution should return a new linked list which is identical to the given list in terms of its structure and contents, and it should not use any nodes of the list.

Input : 1 —> 2 —> 3 —> 4 —> 5 —> None
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

	def clone(self, head: Node) -> Node:
		n=head
		
		if n==None:
			return None
		
		list1=[]
		
		while n!=None:
			list1.append(n.data)
			n=n.next
			
		m=Node(list1[0])
		head=m
		
		length=len(list1)
		
		for i in range(1,length):
			hh=Node(list1[i])
			m.next=hh
			m=m.next
			
		return head
