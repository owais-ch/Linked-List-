'''

Given a singly-linked list of integers, rearrange it by separating odd nodes from even ones. The solution should return a list containing all even nodes followed by all odd nodes, where the relative order of even and odd nodes is maintained.

Input : 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> None
Output: 2 —> 4 —> 6 —> 1 —> 3 —> 5 —> 7 —> None

Input : 2 —> 4 —> 6 —> None
Output: 2 —> 4 —> 6 —> None

Input : 1 —> 3 —> 5 —> 7 —> None
Output: 1 —> 3 —> 5 —> 7 —> None

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def rearrange(self, head: Node) -> Node:
		
		n=head
		
		if n==None:
			return None
		
		list1=[]
		list2=[]
		
		while n!=None:
			if n.data%2!=0:
				list1.append(n)
			else:
				list2.append(n)
			n=n.next
				
		list3=list2+list1
		
		length=len(list3)
		
		m=list3[0]
		head=m
		
		for i in range(1,length):
			hh=list3[i]
			m.next=hh
			m=m.next
			
		m.next=None
		
		return head
