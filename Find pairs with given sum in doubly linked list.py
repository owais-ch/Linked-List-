'''
Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target.

Example 1:

Input:  
1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
target = 7
Output: (1, 6), (2,5)
Explanation: We can see that there are two pairs 
(1, 6) and (2,5) with sum 7.
'''

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        n=head
        
        while n.next!=None:
            n=n.next
            
        m=head
        
        list1=[]
        
        while m!=None and n!=None and m.data<n.data:
            if m.data+n.data==target:
                list1.append([m.data,n.data])
                m=m.next
                n=n.prev
            elif m.data+n.data>target:
                n=n.prev
            elif m.data+n.data<target:
                m=m.next
                
        return list1
 
