'''Reverse a linked list from position m to n.

For example:

Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.'''

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
	def reverseBetween(self, head, B, C):
        n=head
        head=n
        if n.next==None:
            return head
        count=0
        index=1
        list1=[]
        while n!=None:
            if index==B or count==1:
                list1.append(n.val)
                count=1
                if index==C:
                    count=0
            index+=1
            n=n.next
        list1.reverse()
        
        m=head
        head=m

        count=0
        count2=0
        index=1
        while m!=None:
            if index==B or count==1:
                m.val=list1[count2]
                count2+=1
                count=1
                if index==C:
                    count=0
            m=m.next
            index+=1
        return head
