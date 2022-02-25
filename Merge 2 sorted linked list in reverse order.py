'''Given two linked lists of size N and M, which are sorted in non-decreasing order. The task is to merge them in such a way that the resulting list is in decreasing order.

Input:
First line of input contains number of testcases T. For each testcase, first line of input conatains length of both linked lists N and M respectively. Next two lines
contains N and M elements of two linked lists.'''

def mergeResult(h1,h2):
    n=h1
    list1=[]
    
    while n!=None:
        list1.append(n)
        n=n.next
        
    m=h2
    
    while m!=None:
        list1.append(m)
        m=m.next
        
    list1.sort(key=lambda x:x.data,reverse=True)
    
    q=list1[0]
    head=q
    
    for i in range(1,len(list1)):
        hh=list1[i]
        q.next=hh
        q=q.next
    q.next=None    
    return head
