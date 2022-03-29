'''

Given two sorted singly-linked lists of integers, merge them without modifying the links of the first list.

If m and n are the total number of nodes in the first and second list, then the first m smallest nodes in both lists combined should become part of the first list, and the remaining nodes should become part of the second list. The solution should preserve the sorted order of elements in both lists.

Input:

X: 2 —> 6 —> 9 —> 10 —> 15 —> None
Y: 1 —> 4 —> 5 —> 20 —> None

Output:

X: 1 —> 2 —> 4 —> 5 —> 6 —> None
Y: 9 —> 10 —> 15 —> 20 —> None

Note: The solution should rearrange the first list X without modifying its links, and return the second list Y.

'''

class Solution:
	def sortedMerge(self, X: Node, Y: Node) -> Node:
		n=X
		list1=[]
		
		while n!=None:
			list1.append(n.data)
			n=n.next
			
		m=Y	
		
		while m!=None:
			list1.append(m.data)
			m=m.next
			
		list1.sort()
		
		i=0
		
		n=X
		head1=n
		while n!=None:
			n.data=list1[i]
			i+=1
			n=n.next
			
		m=Y
		head2=Y
		
		while m!=None:
			m.data=list1[i]
			m=m.next
			i+=1
			
		return head2
