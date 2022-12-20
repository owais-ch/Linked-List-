'''
Given a sorted linked list of distinct nodes (no two nodes have the same data) and an integer X. Count distinct triplets in the list that sum up to given integer X.
Note: The Linked List can be sorted in any order.

Example 1:

Input: LinkedList: 1->2->4->5->6->8->9, X = 17
Output: 2
Explanation: Distinct triplets are (2, 6, 9) 
and (4, 5, 8) which have sum equal to X i.e 17.
'''

def countTriplets(head,x):
    def traversal(head):
        n=head
        
        while n!=None:
            list1.append(n.val)
            n=n.nxt
            
    list1=[]
    
    traversal(head)
    
    length=len(list1)
    
    count=0
    list1.sort()
    for i in range(length-2):
        j=i+1;k=length-1
        
        while j<k:
            if list1[i]+list1[j]+list1[k]==x:
                count+=1
                j+=1
                k-=1
                
            elif list1[i]+list1[j]+list1[k]>x:
                k-=1
            elif list1[i]+list1[j]+list1[k]<x:
                j+=1
                
    return count
