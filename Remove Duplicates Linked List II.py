'''

Given an unsorted linked list of integers, remove duplicate nodes from it by traversing the list only once. The solution should preserve the order of elements appearing in the list.

Input: 5 —> 3 —> 4 —> 2 —> 5 —> 4 —> 1 —> 3 —> None
Output: 5 —> 3 —> 4 —> 2 —> 1 —> None

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
		head1=m
		
		if n==None:
			return None
			
		list1=[m.data]
		
		while n!=None:
			if n.data not in list1:
				m.next=n
				m=m.next
			list1.append(n.data)	
			n=n.next
		m.next=None	
		return head1
			
