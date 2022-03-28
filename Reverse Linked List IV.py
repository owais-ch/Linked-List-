'''

Given a singly-linked list and two positive numbers m and n where m <= n, reverse the portion of list from position m to n. 

Input:

Linked List: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> None

m = 2 (start position)
n = 5 (end position)

Output: 1 —> 5 —> 4 —> 3 —> 2 —> 6 —> 7 —> None

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def reverse(self, head: Node, m: int, n: int) -> Node:
		q=head
		if head==None:
			return None
		list1=[]
		
		while q!=None:
			list1.append(q)
			q=q.next
			
		list1[m-1:n]=list1[m-1:n][::-1]
		
		q=list1[0]
		head=q
		
		length=len(list1)
		
		for i in range(1,length):
			hh=list1[i]
			q.next=hh
			q=q.next
			
		q.next=None
		
		return head
			
