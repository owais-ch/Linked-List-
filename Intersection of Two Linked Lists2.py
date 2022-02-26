'''Given two linked lists, the task is to complete the function findIntersection(), that returns the intersection of two linked lists. Each of the two linked list
contains distinct node values.

Example 1:

Input:
LinkedList1: 9->6->4->2->3->8
LinkedList2: 1->2->8->6
Output: 6 2 8'''

from collections import OrderedDict

class Solution:
    def findIntersection(self, head1, head2):
        n=head1
        dict1=OrderedDict()
        
        while n!=None:
            if n.data not in dict1:
                dict1[n.data]=1
            
            n=n.next
            
        m=head2
        dict2=OrderedDict()
        
        while m!=None:
            if m.data not in dict2:
                dict2[m.data]=1
            m=m.next
            
        list1=[]    
        
        for i in dict1:
            if i in dict2:
                list1.append(i)
                
        q=Node(list1[0])
        head=q
        
        for i in range(1,len(list1)):
            hh=Node(list1[i])
            q.next=hh
            q=q.next
            
        return  head
