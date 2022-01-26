'''Given a linked list A of length N and an integer B.

You need to reverse every alternate B nodes in the linked list A.'''

class Solution:
    def solve(self, head, B):
        n=head

        list1=[]

        while n!=None:
            list1.append(n)
            n=n.next

        length=len(list1)

        count=0
        for i in range(0,length,B):
            if count%2==0:
                list1[i:i+B]=list1[i:i+B][::-1]

            count+=1

        m=list1[0]
        head=m

        for i in range(1,length):
            hh=list1[i]
            m.next=hh
            m=m.next

        m.next=None
        return head
