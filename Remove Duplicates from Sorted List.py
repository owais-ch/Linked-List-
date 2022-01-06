'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]'''

class Solution:
    def deleteDuplicates(self, head):
        n=head
        if head==None:
            return None
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        list1=sorted(list(set(list1)))
        length=len(list1)
        
        n=ListNode(list1[0])
        head=n
        
        if length==1:
            return head
        else:
            for i in range(1,length):
                hh=ListNode(list1[i])
                n.next=hh
                n=hh
                
        return head
