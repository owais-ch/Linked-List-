'''Given a Linked List, find the element at the kth position.

Example
List: 1→3→4→7
k: 2
Answer: 3'''



class Solution:
	def kthElement(self, head: ListNode, k: int) -> ListNode:
		n=head
		
		count=0
		
		while n!=None:
			count+=1
			
			if count==k:
				return n
			n=n.next
