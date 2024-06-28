'''
Is Linked List Sorted (GFG)
Given a linked list of size n, you have to find whether the given linked list is sorted or not.
The sorting can either be non-increasing or non-decreasing.

Example 1:

Input:
LinkedList: 5->5->6->7->8
Output: 1
'''

def isSorted(head):
    n=head
    m=head
    
    count1=0
    count2=0
    
    while n!=None:
        n=n.next
        
        if n!=None and n.data<m.data:
            count1+=1
        elif n!=None and n.data>m.data:
            count2+=1
            
        if count1>0 and count2>0:
            return 0
            
        m=m.next
        
    return 1



