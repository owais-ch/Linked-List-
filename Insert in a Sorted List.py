'''Given a linked list sorted in ascending order and an integer called data, insert data in the linked list such that the list remains sorted.

Example 1:

Input:
LinkedList: 25->36->47->58->69->80
data: 19
Output: 19 25 36 47 58 69 80'''

class Solution:
    def sortedInsert(self, head1,key):
        n=head1
        
        list1=[]
        
        while n!=None:
            list1.append(n.data)
            n=n.next
            
        list1.append(key)
        list1.sort()
        
        length=len(list1)
        
        m=Node(list1[0])
        head=m
        
        for i in range(1,length):
            hh=Node(list1[i])
            m.next=hh
            m=m.next
            
        return head
