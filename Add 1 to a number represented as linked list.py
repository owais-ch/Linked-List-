'''A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

Example 1:

Input:
LinkedList: 4->5->6
Output: 457 '''

class Solution:
    def addOne(self,head):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n.data)
            n=n.next
          
        number=int(''.join(list(map(str,list1))))+1
        
        list2=list(map(int,list(str(number))))
        
        length=len(list2)
        
        m=Node(list2[0])
        head=m
        
        for i in range(1,length):
            hh=Node(list2[i])
            m.next=hh
            m=m.next
        
        return head
