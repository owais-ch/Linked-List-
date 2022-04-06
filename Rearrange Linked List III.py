 '''

Given a singly-linked list of integers, split it into two lists where each list contains alternating elements from the list. The solution should join the two lists back together and return it.

Input : 1 —> 2 —> 3 —> 4 —> None
Output: 1 —> 3 —> 2 —> 4 —> None

Input : 1 —> 2 —> 3 —> 4 —> 5 —> None
Output: 1 —> 3 —> 5 —> 2 —> 4 —> None

'''

class Solution:
	def rearrange(self, head: Node) -> None:
		n=head
		if n==None:
			return None
        i=0

        list1=[]
        list2=[]

        while n!=None:
            if i%2==0:
                list1.append(n)
            else:
                list2.append(n)

            n=n.next

            i+=1


        list3=list1+list2
        
        length=len(list1)+len(list2)
        
        m=list3[0]
        head=m
        
        for i in range(1,length):
            hh=list3[i]
            m.next=hh
            m=m.next
            
        m.next=None
        
        return head
