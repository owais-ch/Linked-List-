'''

Given two singly-linked lists of integers, merge their nodes into the first list by taking nodes alternately between the two lists. If the first list runs out, the remaining nodes of the second list should not be moved. The solution should return a list containing the first list and the second list.

Input:

X: 1 —> 2 —> 3 —> None
Y: 4 —> 5 —> 6 —> 7 —> 8 —> None

Output: (1 —> 4 —> 2 —> 5 —> 3 —> 6 —> None, 7 —> 8 —> None)

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def shuffleMerge(self, X: Node, Y: Node) -> Tuple[Node]:
		n=X
		if X==None:
			return (None,Y)
		list1=[]
		while n!=None:
			list1.append(n)
			n=n.next
			
		m=Y
		
		list2=[]
		
		while m!=None:
			list2.append(m)
			m=m.next
			
		length=min(len(list1),len(list2))
		
		q=list1[0]
		head1=q
		
		if Y==None:
			return (head1,None)
		
		
		q.next=list2[0]
		q=q.next
		
		for i in range(1,length):
			hh=list1[i]
			q.next=hh
			q=q.next
			
			hh=list2[i]
			q.next=hh
			q=q.next
		
		if len(list1)==len(list2):
			
			return (head1,None)
		elif len(list1)<len(list2):
			
			q.next=None
			head2=list2[length]
			return (head1,head2)
		else:
			length2=len(list1)
			
			for i in range(length,length2):
				q.next=list1[i]
				q=q.next
			q.next=None
			return (head1,None)
