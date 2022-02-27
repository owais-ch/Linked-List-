'''Given a linked list and a value x, partition it such that all nodes less than x come first, then all nodes with value equal to x and finally nodes with value
greater than or equal to x. The original relative order of the nodes in each of the three partitions should be preserved. The partition must work in-place.
 
Example 1:
Input:
1->4->3->2->5->2->3,
x = 3
Output:
1->2->2->3->3->4->5
Explanation: 
Nodes with value less than 3 come first, 
then equal to 3 and then greater than 3.'''

class Solution:
    def partition(self, head, x):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n)
            n=n.next
        
        list2=[]
        list3=[]
        list4=[]
        for i in list1:
            if i.data<x:
                list2.append(i)
            elif i.data==x:
                list3.append(i)
            else:
                list4.append(i)
                
        list5=list2+list3+list4
        
        m=list5[0]
        head=m
        length=len(list5)
        
        for i in range(1,length):
            hh=list5[i]
            m.next=hh
            m=m.next
            
        m.next=None
        
        return head
