'''Given a singly linked list of size N, and an integer K. You need to swap the Kth node from the beginning and Kth node from the end of the linked list.
Swap the nodes through the links. Do not change the content of the nodes.

 

Example 1:

Input:
N = 4,  K = 1
value[] = {1,2,3,4}
Output: 1
Explanation: Here K = 1, hence after
swapping the 1st node from the beginning
and end thenew list will be 4 2 3 1.'''


def swapkthnode(head,num,k):
    list1=[]
    n=head
    
    while n!=None:
        list1.append(n)
        n=n.next
        
    length=len(list1)
    if k>length:
        return head
    list1[k-1],list1[-k]=list1[-k],list1[k-1]
    
    n=list1[0]
    head=n
    
    for i in range(1,length):
        hh=list1[i]
        n.next=hh
        n=n.next
    
    n.next=None
        
    
    return head
