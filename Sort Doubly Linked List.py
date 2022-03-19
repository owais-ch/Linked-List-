'''

Given a doubly-linked list of integers, rearrange its nodes to be sorted in increasing order.

Input : 6 ⇔ 3 ⇔ 4 ⇔ 8 ⇔ 2 ⇔ 9 ⇔ None
Output: 2 ⇔ 3 ⇔ 4 ⇔ 6 ⇔ 8 ⇔ 9 ⇔ None

Input : 9 ⇔ -3 ⇔ 5 ⇔ -2 ⇔ -8 ⇔ -6 ⇔ None
Output: -8 ⇔ -6 ⇔ -3 ⇔ -2 ⇔ 5 ⇔ 9 ⇔ None

'''

class Solution:

	'''
	A doubly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, prev=None, next=None):
			self.data = data	# data field
			self.prev = prev	# pointer to the previous node
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
