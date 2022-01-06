'''Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]'''

class Solution:
    def rotateRight(self, head, k):
        n=head
        if n==None:
            return None
        elif n.next==None:
            return head
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        m=len(list1)
        
        if k==0 or k%m==0:
            return head
        if k>m:
            k=k%m    
            
        list1=list1[-k:]+list1[:m-k]
        length=len(list1)
        
        m=ListNode(list1[0])
        head=m
        for i in range(1,length):
            hh=ListNode(list1[i])
            m.next=hh
            m=hh
            
        return head
