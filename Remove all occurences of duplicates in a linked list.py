'''Given a sorted linked list, delete all nodes that have duplicate numbers (all occurrences), leaving only numbers that appear once in the original list. 

Example 1:

Input: 
N = 8
Linked List = 23->28->28->35->49->49->53->53
Output: 
23 35
Explanation:
The duplicate numbers are 28, 49 and 53 which 
are removed from the list.'''


from collections import Counter
class Solution:
    def removeAllDuplicates(self, head):
        n=head
        list1=[]
        
        while n!=None:
            list1.append(n.data)
            n=n.next
        dict1=Counter(list1)
        
        list2=[i for i in list1 if dict1[i]==1]
        list2.sort()
        length=len(list2)
        
        m=Node(list2[0])
        head=m
        for i in range(1,length):
            hh=Node(list2[i])
            m.next=hh
            m=m.next
            
        return head
