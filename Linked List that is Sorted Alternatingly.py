'''Given a Linked list of size N, the list is in alternating ascending and descending orders. Sort the given linked list in non-decreasing order.

Example 1:

Input:
LinkedList: 1->9->2->8->3->7
Output: 1 2 3 7 8 9
Explanation: After sorting the given
list will be 1-> 2-> 3-> 7-> 8-> 9.'''

def sort(h1):
    n=h1
    list1=[]
    while n!=None:
        list1.append(n)
        n=n.next
        
    list1=sorted(list1,key=lambda x:x.data)
    
    length=len(list1)
    
    m=list1[0]
    head=m
    
    for i in range(1,length):
        hh=list1[i]
        m.next=hh
        m=m.next
    m.next=None    
    return head
