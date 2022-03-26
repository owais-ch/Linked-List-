'''Given a singly-linked list and a positive number k, reverse every alternate group of k nodes. The swapping of data is not allowed, only links should be changed.


Input:

Linked List: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> 8 —> 9 —> 10 —> None
k = 2

Output: 2 —> 1 —> 3 —> 4 —> 6 —> 5 —> 7 —> 8 —> 10 —> 9 —> None


Input:

Linked List: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> 8 —> 9 —> 10 —> None
k = 3

Output: 3 —> 2 —> 1 —> 4 —> 5 —> 6 —> 9 —> 8 —> 7 —> 10 —> None


Input:

Linked List: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> 8 —> 9 —> 10 —> None
k >= 10

Output: 10 —> 9 —> 8 —> 7 —> 6 —> 5 —> 4 —> 3 —> 2 —> 1 —> None

'''

class Solution:
	def reverseAlternatingKNodes(self, head: Node, k: int) -> Node:
		n=head
		if n==None:
			return None
		list1=[]
		
		while n!=None:
			list1.append(n)
			n=n.next
			
		length=len(list1)
		
		for i in range(0,length,2*k):
			list1[i:i+k]=list1[i:i+k][::-1]
			
		m=list1[0]
		head=m
		
		for i in range(1,length):
			hh=list1[i]
			m.next=hh
			m=m.next
			
		m.next=None
		
	    return head
