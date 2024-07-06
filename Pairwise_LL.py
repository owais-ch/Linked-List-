'''
Pairwise swap of nodes in LinkedList (GFG)

Given a linked list of N positive integers. You need to swap elements pairwise. Your task is to complete the function pairwise_swap().

Example 1:

Input:
N = 7
value[] = {1,2,3,4,5,6,7}
Output: 2 1 4 3 6 5 7
Explanation:The linked list after swapping
becomes: 1 2 3 4 5 6 7 -> 2 1 4 3 6 5 7.
'''
def pairwiseSwap(head):
    n=head
    m=n.next
    
    count=0
    
    while n!=None and m!=None:
        if count==0:
            n.next=m.next
            m.next=n
            head=m
            m=n.next
            count+=1
        else:
            if count>1:
                n=n.next
                m=m.next
            if n==None or m==None:
                return head
                
            if m.next==None:
                return head
                
            n.next=m.next
            n=n.next
            m.next=n.next
            n.next=m
            count+=1
    
    if n!=None:
        n.next=None  
    if m!=None:
        m.next=None
    return head
