'''Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]'''

class Solution:
    def sortList(self, head):
        n=head
        
        if n==None:
            return None
        elif n.next==None:
            return n
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        list1.sort()
        
        length1=len(list1)
        
        m=ListNode(list1[0])
        head=m
        
        for i in range(1,length1):
            hh=ListNode(list1[i])
            m.next=hh
            m=m.next
            
        return head
