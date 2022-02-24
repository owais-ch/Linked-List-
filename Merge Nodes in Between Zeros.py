'''You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

 

Example 1:


Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.'''

class Solution:
    def mergeNodes(self, head):
        n=head
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        length=len(list1)
        
        list2=[]
        list3=[]
        count=0
        for i in range(length):
            if list1[i]==0 and count==0:
                count=1
            elif list1[i]!=0 and count==1:
                list2.append(list1[i])
            elif list1[i]==0 and count==1:
                list3.append(sum(list2))
                list2=[]
                
        length=len(list3)
        
        m=ListNode(list3[0])
        head=m
        for i in range(1,length):
            hh=ListNode(list3[i])
            m.next=hh
            m=m.next
            
        return head
