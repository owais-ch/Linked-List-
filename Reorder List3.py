'''Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You must do this in-place without altering the nodes’ values.

For example,

Given {1,2,3,4}, reorder it to {1,4,2,3}.'''

class Solution:
	def reorderList(self, head):
        n=head

        list1=[]

        while n!=None:
            list1.append(n)
            n=n.next

        length=len(list1)

        list2=list1[::-1]

        m=list1[0]
        head=m
        count1=1
        count2=0

        for i in range(1,length):
            if i%2!=0:
                hh=list2[count2]
                m.next=hh
                m=m.next
                count2+=1
            else:
                hh=list1[count1]
                m.next=hh
                m=m.next
                count1+=1

        m.next=None

        return head
