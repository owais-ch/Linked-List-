'''Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list. If the number of nodes is not a multiple
of k then left-out nodes, in the end, should be considered as a group and must be reversed (See Example 2 for clarification).

Example 1:

Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5 
Explanation: 
The first 4 elements 1,2,2,4 are reversed first 
and then the next 4 elements 5,6,7,8. Hence, the 
resultant linked list is 4->2->2->1->8->7->6->5.'''



class Solution:
    def reverse(self,head, k):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n)
            n=n.next
            
        length=len(list1)
        
        for i in range(0,length,k):
            list1[i:i+k]=list1[i:i+k][::-1]
            
        m=list1[0]
        head=m
        
        for i in range(1,length):
            hh=list1[i]
            m.next=hh
            m=m.next
            
        m.next=None
        
        return head
