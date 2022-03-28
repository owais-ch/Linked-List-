'''

Given a doubly-linked list of integers, reverse it and return the reversed list. The swapping of data is not allowed, only links should be changed.

Input : 1 ⇔ 2 ⇔ 3 ⇔ 4 ⇔ 5 ⇔ None
Output: 5 ⇔ 4 ⇔ 3 ⇔ 2 ⇔ 1 ⇔ None

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

	def reverse(self, head: Node) -> Node:
		n=head
		if n==None:
			return None
		list1=[]
		
		while n!=None:
			list1.append(n)
			n=n.next
			
		list1.reverse()
		
		length=len(list1)
		
		m=list1[0]
		m.prev=None
		
		head=m
		
		for i in range(1,length):
			hh=list1[i]
			m.next=hh
		    hh.prev=m
		    m=m.next
		m.next=None    
		return head
