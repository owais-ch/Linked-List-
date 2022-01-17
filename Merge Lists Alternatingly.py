'''Given two linked lists, your task is to complete the function mergeList() which inserts nodes of second list into first list at alternate positions of first list.

Input:
First line of input contains number of testcases T. For each testcase there will be 4 lines. First line consists of the length of the first linked list, next line contains
elements of the linked list inreverse order. Third line contains length of another linked list and next line contains elements of the linked list.'''

def mergeList(head1, head2):
    n=head1
    
    m=head2
    
    temp1=head1
    temp2=head2
    
    head3=n
    
    while temp1!=None:
        temp1=temp1.next
        n.next=temp2
        n=n.next
        temp2=temp2.next
        n.next=temp1
        n=n.next
        if temp1==None or temp2==None:
            break
    if temp2!=None:
        m=temp2
        head4=m
    else:
        head4=None
        
        
    return head3,head4
