'''Given two linked lists that represent two large positive numbers. The task is to subtract the given two numbers represented by the linked list. Subtract the smaller 
from the larger one.

Example 1:

Input:
L1 = 1->0->0
L2 = 1->2
Output: 8 8
Explanation:  12 subtracted from 100
gives us 88 as result.'''

def subLinkedList(l1, l2): 
    n=l1
    
    list1=[]
    
    while n!=None:
        list1.append(n.data)
        n=n.next
        
    number1=int(''.join(list(map(str,list1))))
    
    m=l2
    
    list2=[]
    
    while m!=None:
        list2.append(m.data)
        m=m.next
        
    number2=int(''.join(list(map(str,list2))))
    
    if number1>number2:
        number3=number1-number2
    else:
        number3=number2-number1
        
    list3=list(map(int,list(str(number3))))
    
    length=len(list3)
    
    q=Node(list3[0])
    head=q
    
    for i in range(1,length):
        hh=Node(list3[i])
        q.next=hh
        q=q.next
        
    return head
