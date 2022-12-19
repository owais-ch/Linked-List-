'''
Given two string, represented as linked lists (every character is a node->data in the linked list). Write a function compare() that works similar to strcmp(),
i.e., it returns 0 if both strings are same, 1 if first linked list is lexicographically greater, and -1 if second is lexicographically greater.

Input:
First line of input contains number of testcases T. For each testcase, there will be 4 lines of input. First line of which contains length of first linked list and
next line contains the linked list, similarly next two lines contains length and linked list respectively.

Output:
Comapare two strings represented as linked list.
'''

def compare(head1, head2):
    n=head1
    m=head2
    
    while n!=None and m!=None:
        if n.data>m.data:
            return 1
        elif n.data<m.data:
            return -1
        n=n.next
        m=m.next
        
    if n==None and m==None:
        return 0
    elif n!=None:
        return 1
    else:
        return -1
