'''

Given a singly-linked list of integers and a positive number k, swap the k'th node from the beginning with the k'th node from the end. The swapping should be done so that only links between the nodes are exchanged, and no data is swapped.

Input:

Linked List: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> 8 —> None
k = 2

Output: 1 —> 7 —> 3 —> 4 —> 5 —> 6 —> 2 —> 8 —> None


Input:

Linked List: 1 —> 2 —> None
k = 2

Output: 2 —> 1 —> None


Assume that k is less than or equal to the length of linked list.

'''

class Solution:
	def swapNodes(self, head: Node, k: int) -> Node:
		n=head
		if n==None:
			return None
		list1=[]
		
		while n!=None:
			list1.append(n)
			n=n.next
			
		length=len(list1)	
		
		list1[k-1],list1[length-k]=list1[length-k],list1[k-1]
		
		m=list1[0]
		head=m
		
		for i in range(1,length):
			hh=list1[i]
			m.next=hh
			m=m.next
			
		m.next=None
		
		return head
