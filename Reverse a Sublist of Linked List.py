'''
Problem Statement
You are given a linked list of 'N' nodes. Your task is to reverse the linked list from position 'X' to 'Y'.
For Example:
Assuming, the linked list is 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> NULL. X = 2 and Y = 5. On reversing the given linked list from position 2 to 5, we get 10 -> 50 -> 40 -> 30 -> 20 -> 60 -> NULL.
Input Format:
The first line of input contains an integer ‘T’ representing the number of test cases.

The first line of every test case contains the elements of the linked list separated by a single space and terminated by -1. Hence, -1 would never be a list element.

The second line of every test case contains two space-separated integers, 'X' and 'Y', denoting the positions in the linked list.
'''

def reverseSublist(head, x, y):
    i=1
    n=head
    q=head
    head1=q
    if x>1:
        while x-1!=i:
            n=n.next
            q=q.next
            i+=1
        first=n
        n=n.next
    
    prev=None
    curr=n
    next1=None
    count=0
    length=y-x+1
    while count<length and curr!=None:
        next1=curr.next
        curr.next=prev
        prev=curr
        curr=next1
        count+=1
    if next1==None and x==1:
        head1=prev
        return head1
    elif x==1:
        head1=prev
        hh=head1
        while hh.next!=None:
            hh=hh.next
        hh.next=next1
        return head1
    last=next1
    q.next=prev
    while q.next!=None:
        q=q.next
    q.next=next1
    
    return head1
