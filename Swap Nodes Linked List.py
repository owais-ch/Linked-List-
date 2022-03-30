'''

Given a singly-linked list of integers, pairwise swap its adjacent nodes. The swapping of data is not allowed, only links should be changed.

Input : 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> 8 —> None
Output: 2 —> 1 —> 4 —> 3 —> 6 —> 5 —> 8 —> 7 —> None

'''

class Solution:
	def rearrange(self, head: Node) -> Node:
		n=head
		
		if n==None:
			return None
			
		list1=[]
		
		while n!=None:
			list1.append(n)
			n=n.next
			
		length=len(list1)
		
		for i in range(0,length,2):
			list1[i:i+2]=list1[i:i+2][::-1]
			
		m=list1[0]
		head=m
		for i in range(1,length):
			hh=list1[i]
			m.next=hh
			m=m.next
			
		m.next=None
		
		return head
