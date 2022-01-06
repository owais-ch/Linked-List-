'''You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6'''

class Solution:
    def mergeKLists(self, lists):
        length=len(lists)
        
        list1=[]
        
        for i in range(length):
            n=lists[i]
            
            while n!=None:
                list1.append(n.val)
                n=n.next
                
        list1.sort()
        
        length2=len(list1)
        
        if length2==0:
            return None
        else:
            m=ListNode(list1[0])
            head=m
            
            for i in range(1,length2):
                hh=ListNode(list1[i])
                m.next=hh
                m=m.next
                
            return head
