'''Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all
zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.'''


class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n.data)
            n=n.next
            
        list1.sort()
        length=len(list1)
        
        m=Node(list1[0])
        head=m
        
        for i in range(1,length):
            hh=Node(list1[i])
            m.next=hh
            m=m.next
         
        return head
