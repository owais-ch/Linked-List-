'''Given a singly linked list of size N. The task is to swap elements in the linked list pairwise.
For example, if the input list is 1 2 3 4, the resulting list after swaps will be 2 1 4 3.
Note: You need to swap the nodes, not only the data. If only data is swapped then driver will print -1.

Example 1:

Input:
LinkedList: 1->2->2->4->5->6->7->8
Output: 2 1 4 2 6 5 8 7
Explanation: After swapping each pair
considering (1,2), (2, 4), (5, 6).. so
on as pairs, we get 2, 1, 4, 2, 6, 5,
8, 7 as a new linked list.

'''


class Solution:    
    def pairWiseSwap(self, head):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n)
            n=n.next
            
        length=len(list1)
        if length==1:
            return head
        
        if length%2!=0:
            length2=length-1
        else:
            length2=length
        
        for i in range(0,length2,2):
            list1[i],list1[i+1]=list1[i+1],list1[i]
            
            
        m=list1[0]
        head=m
        
        for i in range(1,length):
            hh=list1[i]
           
            m.next=hh
            
            m=m.next
        if length%2==0:    
            m.next=None
        else:
            m.next=list1[-1]
            m=m.next
            m.next=None
        return head
