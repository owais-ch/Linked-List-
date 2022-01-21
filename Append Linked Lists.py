'''Given two Linked Lists, append second Linked List to end of first Linked List and return the first list.

Example
List 1: 1→3→4→7
List 2: 6→2→5
Result: 1→3→4→7→6→2→5'''

class Solution:
	def appendLists(self, list1, list2):
		n=list1
		list1=n
		
		while n.next!=None:
			n=n.next
			
		n.next=list2
		
		return list1
