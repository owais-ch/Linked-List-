'''Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]'''

class Solution:
    def partition(self, head, x):
        n=head
        if n==None:
            return None
        elif n.next==None:
            return n
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        less=[i for i in list1 if i<x]
        great=[i for i in list1 if i>=x]
        
        length1=len(less)
        
        length2=len(great)
        
        if length1>0:
            m=ListNode(less[0])
            head=m
        
            for i in range(1,length1):
                hh=ListNode(less[i])
                m.next=hh
                m=m.next
            
            for i in range(length2):
                hh=ListNode(great[i])
                m.next=hh
                m=m.next
            
            return head
        else:
            m=ListNode(great[0])
            head=m
            for i in range(1,length2):
                hh=ListNode(great[i])
                m.next=hh
                m=m.next
            
            return head
