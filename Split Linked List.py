'''

Given a singly-linked list of integers, split it into two sublists – one for the front half and one for the back half. The solution should return a tuple of the front half and the back half.

Input: 2 —> 3 —> 5 —> 7 —> None
Output: ([2 —> 3 —> None], [5 —> 7 —> None])

If the total number of elements in the list is odd, the extra element should go in the front list.

Input: 2 —> 3 —> 5 —> 7 —> 9 —> None
Output: ([2 —> 3 —> 5 —> None], [7 —> 9 —> None])

'''
from math import ceil
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
		
		half1=ceil(length/2)
		
		half2=length-half1
		
		m1=list1[0]
		head1=m1
		
		for i in range(1,half1):
			hh=list1[i]
			m1.next=hh
			m1=m1.next
		m1.next=None
		
		if half2==0:
			return (head1,None)
		m2=list1[half1]
		head2=m2
		
		for i in range(half1,length):
			hh=list1[i]
			m2.next=hh
			m2=m2.next
			
		m2.next=None
		
		return (head1,head2)
