'''Given an unsorted linked list of N nodes. The task is to remove duplicate elements from this unsorted Linked List. When a value appears in multiple nodes, 
the node which appeared first should be kept, all others duplicates are to be removed.

Example 1:

Input:
N = 4
value[] = {5,2,2,4}
Output: 5 2 4
Explanation:Given linked list elements are
5->2->2->4, in which 2 is repeated only.
So, we will delete the extra repeated
elements 2 from the linked list and the
resultant linked list will contain 5->2->4'''

class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n.data)
            n=n.next
            
        length=len(list1)  
        
        list2=[]
        dict1=dict()
        
        for i in range(length):
            if list1[i] not in dict1:
                dict1[list1[i]]=1
                list2.append(list1[i])
            
        length2=len(list2)  
        
        m=Node(list2[0])
        head=m
        
        for i in range(1,length2):
            hh=Node(list2[i])
            m.next=hh
            m=m.next
            
        return head
