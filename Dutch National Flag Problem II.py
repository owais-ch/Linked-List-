'''

Given a singly-linked list containing 0’s, 1’s, and 2’s, sort the linked list by doing a single traversal of it.

Input : 0 —> 1 —> 2 —> 2 —> 1 —> 0 —> 0 —> 2 —> 0 —> 1 —> 1 —> 0 —> None
Output: 0 —> 0 —> 0 —> 0 —> 0 —> 1 —> 1 —> 1 —> 1 —> 2 —> 2 —> 2 —> None

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def sort(self, head: Node) -> Node:
		n=head
		list1=[]
		
		while n!=None:
			list1.append(n.data)
			n=n.next
			
		list1.sort()
		
		n=head
		i=0
		while n!=None:
			n.data=list1[i]
			n=n.next
			i+=1
			
		return head
			
