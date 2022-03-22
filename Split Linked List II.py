'''

Given a singly-linked list of integers, split it into two lists containing alternating elements from the original list.

Input: 1 —> 2 —> 3 —> 4 —> None
Output: ([1 —> 3 —> None], [2 —> 4 —> None])

Input: 1 —> 2 —> 3 —> 4 —> 5 —> None
Output: ([1 —> 3 —> 5 —> None], [2 —> 4 —> None])

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def frontBackSplit(self, head: Node) -> Tuple[Node]:
		n=head
		
		if n==None:
			return (None,None)
			
		list1=[]
		
		while n!=None:
			list1.append(n)
			n=n.next
			
		length=len(list1)
		
		m1=list1[0]
		
		head1=m1
		
		for i in range(2,length,2):
			hh=list1[i]
			m1.next=hh
			m1=m1.next
			
		m1.next=None
		
		if length==1:
			return (head1,None)
			
		m2=list1[1]
		
		head2=m2
		
		for i in range(3,length,2):
			hh=list1[i]
			m2.next=hh
			m2=m2.next
			
		m2.next=None
		
		return (head1,head2)
