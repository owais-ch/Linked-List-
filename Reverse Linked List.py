'''Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]'''

class Solution:
    def reverseList(self, head):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        n=head
        head=n
        
        length=len(list1)
        list1.reverse()
        
        for i in range(length):
            n.val=list1[i]
            n=n.next
            
        return head
