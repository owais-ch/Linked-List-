'''
Identical Linked List (GFG)

Given the two singly Linked Lists respectively. The task is to check whether two linked lists are identical or not. 
Two Linked Lists are identical when they have the same data and with the same arrangement too. If both Linked Lists are identical then return true otherwise return false. 

Examples:

Input:
LinkedList1: 1->2->3->4->5->6
LinkedList2: 99->59->42->20
Output: false
'''

def areIdentical(head1, head2):
    n=head1
    m=head2
    
    while n!=None and m!=None:
        if n.data!=m.data:
            return False
        n=n.next
        m=m.next
        
    if n==None and m==None:
        return True
        
    return False
