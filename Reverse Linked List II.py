'''Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, 
and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]'''

class Solution:
    def reverseBetween(self, head, left, right):
        n=head
        head=n
        
        i=0
        list1=[]
        
        while i<right:
            if i>=left-1:
                list1.append(n.val)
            n=n.next
            i+=1
                
        list1.reverse()
        
        i=0
        n=head
        head=n
        j=0
        while i<right:
            if i>=left-1:
                n.val=list1[j]
                j+=1
            n=n.next
            i+=1
            
        return head
