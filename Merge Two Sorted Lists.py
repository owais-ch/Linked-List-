'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]'''

class Solution:
    def mergeTwoLists(self, list1, list2):
        arr1=[]
        
        n=list1
        
        while n!=None:
            arr1.append(n.val)
            n=n.next
            
        m=list2
        
        while m!=None:
            arr1.append(m.val)
            m=m.next
            
        arr1.sort()
        length=len(arr1)
        if length==0:
            return None
        hh=ListNode(arr1[0])
        head=hh
        
        
        
        for i in range(1,length):
            mm=ListNode(arr1[i])
            hh.next=mm
            hh=mm
            
        return head
