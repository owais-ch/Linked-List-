'''

Given two singly-linked lists of integers, merge their nodes to make one list, taking nodes alternately between the two lists.

Input: 1 —> 2 —> 3 —> None, 4 —> 5 —> 6 —> None
Output: 1 —> 4 —> 2 —> 5 —> 3 —> 6 —> None

If either list runs out, all the nodes should be taken from the other list.

Input: 1 —> 2 —> None, 3 —> 4 —> 5 —> None
Output: 1 —> 3 —> 2 —> 4 —> 5 —> None

Input: 1 —> 2 —> 3 —> None, 4 —> None
Output: 1 —> 4 —> 2 —> 3 —> None

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def shuffleMerge(self, X: Node, Y: Node) -> Node:
		if X==None:
			return Y
		elif Y==None:
			return X
		n=X
		
		list1=[]
		
		while n!=None:
			list1.append(n)
			n=n.next
			
		m=Y
		
		list2=[]
		
		while m!=None:
			list2.append(m)
			m=m.next
			
		length1=len(list1)
		length2=len(list2)
		
		min_length=min(length1,length2)
		
		q=list1[0]
		head=q
		q.next=list2[0]
		q=q.next
		
		for i in range(1,min_length):
			hh=list1[i]
			q.next=hh
			q=q.next
			
			hh=list2[i]
			q.next=hh
			q=q.next
			
		if length1==length2:
			q.next=None
			return head
		elif length1>length2:
			for i in range(min_length,length1):
				hh=list1[i]
				q.next=hh
				q=q.next
			q.next=None
			return head
		else:
			for i in range(min_length,length2):
				hh=list2[i]
				q.next=hh
				q=q.next
			q.next=None
			return head
