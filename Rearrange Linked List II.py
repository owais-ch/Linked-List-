'''

Given a singly-linked list of integers, rearrange its nodes such that alternate positions are filled with nodes starting from the beginning and end of the list.

Input : 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> None
Output: 1 —> 6 —> 2 —> 5 —> 3 —> 4 —> None

Input : 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> None
Output: 1 —> 7 —> 2 —> 6 —> 3 —> 5 —> 4 —> None

'''

class Solution:
	def rearrange(self, head: Node) -> None:
		n=head
		if n==None:
			return None
			
		list1=[]
		
		while n!=None:
			list1.append(n)
			n=n.next
			
		length=len(list1)
		
		q=list1[0]
		head=q
		i=0
		count1=1
		count2=1
		while i<length:
			if i%2==0:
				hh=list1[length-count1]
				q.next=hh
				q=q.next
				count1+=1
			else:
				hh=list1[count2]
				q.next=hh
				q=q.next
				count2+=1
				
			i+=1
			
		q.next=None
		
		return head
