'''Given a linked list consisting of L nodes and given a number N. The task is to find the Nth node from the end of the linked list.

Example 1:

Input:
N = 2
LinkedList: 1->2->3->4->5->6->7->8->9
Output: 8
Explanation: In the first example, there
are 9 nodes in linked list and we need
to find 2nd node from end. 2nd node
from end is 8.  

'''

def getNthFromLast(head,n):
    m=head
    
    list1=[]
    
    while m!=None:
        list1.append(m.data)
        m=m.next
        
    length=len(list1)
    
    if n>length:
        return -1
    return list1[-n]
