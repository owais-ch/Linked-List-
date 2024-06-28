'''
Kth from End of Linked List

Given head of a linked list and a number k, your task is to find the kth node from the end. If k is more than the number of nodes, then the output should be -1.
The following is internal representation of every test case (three inputs).
n :  Size of the linked list
k : Postion (from end) of the node to be found
value[] :  An array of values that represents values of nodes.

Examples

Input: n = 9, k = 2, value[] = {1,2,3,4,5,6,7,8,9}
Output: 8
Explanation: The given linked list is 1->2->3->4->5->6->7->8->9. The 2nd node from end is 8.  
'''
def getKthFromLast(head, k):
    length=1
    
    fast=head
    
    while fast.next!=None:
        if fast.next.next!=None:
            length+=2
            fast=fast.next.next
        elif fast.next!=None:
            length+=1
            fast=fast.next
            
        
        
    if k>length:
        return -1
        
    index=length-k
    
    n=head
    
    i=0
    
    while n!=None and i<length-k:
        n=n.next
        i+=1
        
    return n.data
