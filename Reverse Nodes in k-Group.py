'''Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes,
in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]'''

class Solution:
    def reverseKGroup(self, head, k):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
        
        count=0
        length=len(list1)
        
        for i in range(0,length,k):
            if length-count>=k:
                list1[count:count+k]=list1[count:count+k][::-1]
                count+=k
                
        m=ListNode(list1[0])
        head=m
        
        for i in range(1,length):
            hh=ListNode(list1[i])
            m.next=hh
            m=m.next
            
        return head
