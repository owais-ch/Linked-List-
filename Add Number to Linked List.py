'''

Given a single-digit number k and a singly-linked list whose nodes stores digits of a non-negative number, add k to the linked list.

Input: List = 9 —> 9 —> 9 —> 3 —> None, k = 7
Output: 1 —> 0 —> 0 —> 0 —> 0 —> None
Explanation: The input linked list represents the number 9993. Adding a single-digit number 7 results in linked list corresponding to the number 10000.

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def addDigit(self, head: Node, k: int) -> Node:
		n=head
		
		if n==None:
			return Node(k)
		list1=[]
		
		while n!=None:
			list1.append(n.data)
			n=n.next
			
		number=int(''.join(list(map(str,list1))))+k
		
		list1=list(map(int,list(str(number))))
		
		length=len(list1)
		
		m=Node(list1[0])
		head=m
		
		for i in range(1,length):
			hh=Node(list1[i])
			m.next=hh
			m=m.next
			
		m.next=None
		
		return head
