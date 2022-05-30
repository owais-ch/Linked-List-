'''Problem Statement
You have been given a singly Linked List of integers. Your task is to divide this list into two smaller singly-linked lists in which the nodes appear in alternating fashion from the original list.
For Example:
If the given linked list is 1 -> 2 -> 3 -> 4 -> 5 -> NULL

The first sub-list is 1 -> 3 -> 5 -> NULL.
The second sub-list is 2 -> 4 -> NULL.
If it is impossible to make any of the two smaller sub-lists, return an empty list i.e. NULL.
Input Format :
The first line of input contains an integer 'T' representing the number of test cases or queries to be processed. Then the test case follows.

The only line of each test case contains the elements of the singly linked list separated by a single space and terminated by -1. Hence, -1 would never be a list element.
Output Format :
For each test case, print two lines representing the first and second linked lists respectively. The elements of each linked list must be separated by a single space and terminated by -1.
Print output of each test case in a separate line.'''

def divideList(head):
    if head==None:
        return None,None
    elif head.next==None:
        return head,None
    else:
        n=head
        m=head.next
        head1=n
        head2=m
        
        while n!=None and m!=None:
            n.next=n.next.next
            if n.next==None:
                m.next=None
                break
            m.next=m.next.next
            n=n.next
            m=m.next
        return head1,head2
