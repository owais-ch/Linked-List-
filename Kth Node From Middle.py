'''Problem Description

Given a linked list A of length N and an integer B.

You need to find the value of the Bth node from the middle towards the beginning of the Linked List A.

If no such element exists, then return -1.

NOTE:

Position of middle node is: (N/2)+1, where N is the total number of nodes in the list.'''

class Solution:
    def solve(self, head,k):
        n=head

        list1=[]

        i=0
        while n!=None:
            list1.append(n.val)
            n=n.next
            i+=1

        length=i
        middle=length//2+1

        if middle-k-1<0:
            return -1
        else:
            return list1[middle-k-1]
