'''Given a doubly linked list of n elements. The task is to reverse the doubly linked list.

Example 1:

Input:
LinkedList: 3 <--> 4 <--> 5
Output: 5 4 3'''

def reverseDLL(head):
    n=head
    list1=[]
    
    while n!=None:
        list1.append(n)
        n=n.next
        
    list1.reverse()
    
    length=len(list1)
    
    m=list1[0]
    head=m
    for i in range(1,length):
        hh=list1[i]
        m.next=hh
        m=m.next
        
    m.next=None
    return head
