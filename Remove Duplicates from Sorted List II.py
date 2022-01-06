'''Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]'''

from collections import Counter

class Solution:
    def deleteDuplicates(self, head):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        dict1=Counter(list1)
        
        list2=[]
        
        for i in dict1:
            if dict1[i]==1:
                list2.append(i)
        length=len(list2)
        if length==0:
            return None
        
        list2.sort()
        
        m=ListNode(list2[0])
        head=m
        
        
        
        if length==1:
            return head
        else:
            for i in range(1,length):
                hh=ListNode(list2[i])
                m.next=hh
                m=hh
                
        return head
