'''Given a linked list, you have to perform the following task:

Extract the alternative nodes starting from second node.
Reverse the extracted list.
Append the extracted list at the end of the original list.
â€‹Example 1:

Input:
LinkedList = 10->4->9->1->3->5->9->4
Output: 10 9 3 9 4 5 1 4'''

class Solution:
    def rearrange(self, head):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n)
            n=n.next
            
        length=len(list1)
        
        list2=[list1[0]]
        list3=[]
        list4=[]
        for i in range(1,length):
            if i%2!=0:
                list3.append(list1[i])
            else:
                list4.append(list1[i])
                
        list3=list2+list4+list3[::-1]
        
        length=len(list3)
        
        m=list3[0]
        head=m
        
        for i in range(1,length):
            hh=list3[i]
            m.next=hh
            m=m.next
        m.next=None    
        return head
