'''

Given two sorted singly-linked lists of integers, merge them into a single list in decreasing order, and return it. In other words, merge two sorted linked lists from their end.

Input:

X: 1 —> 3 —> 5 —> None
Y: 2 —> 6 —> 7 —> 10 —> None

Output: 10 —> 7 —> 6 —> 5 —> 3 —> 2 —> 1 —> None

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def sortedMerge(self, X: Node, Y: Node) -> Node:
		if X==None and Y==None:
			return None
		n=X
		
		list1=[]
		
		while n!=None:
			list1.append(n)
			n=n.next
			
		m=Y
		
		while m!=None:
			list1.append(m)
			m=m.next
			
		list1.sort(key=lambda x:-(x.data))
		
		length=len(list1)
        
        
        q=list1[0]
        head=q
        
        for i in range(1,length):
        	hh=list1[i]
        	q.next=hh
        	q=q.next
        	
        q.next=None
        
        return head
