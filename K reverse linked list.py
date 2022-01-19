'''Given a singly linked list and an integer K, reverses the nodes of the

list K at a time and returns modified linked list.

NOTE : The length of the list is divisible by K

Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,

You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

Try to solve the problem using constant extra space.'''

class Solution:
	def reverseList(self, head, k):
        n=head

        list1=[]

        while n!=None:
            list1.append(n)
            n=n.next
        
        length=len(list1)

        for i in range(0,length,k):
            list1[i:i+k]=list1[i:i+k][::-1]

        m=list1[0]
        head=m

        for i in range(1,length):
            hh=list1[i]
            m.next=hh
            m=m.next
        m.next=None
        return head
