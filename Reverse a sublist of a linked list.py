'''Given a linked list and positions m and n. Reverse the linked list from position m to n.

Example 1:

Input :
N = 10
Linked List = 1->7->5->3->9->8->10
                      ->2->2->5->NULL
m = 1, n = 8
Output : 2 10 8 9 3 5 7 1 2 5 
Explanation :
The nodes from position 1 to 8 
are reversed, resulting in 
2 10 8 9 3 5 7 1 2 5.'''

class Solution:
    def reverseBetween(self, head, m, n):
        q=head
        list1=[]
        
        while q!=None:
            list1.append(q)
            q=q.next
            
        length=len(list1)
        
        list1[m-1:n]=list1[m-1:n][::-1]
        
        p=list1[0]
        head=p
        for i in range(1,length):
            hh=list1[i]
            p.next=hh
            p=p.next
            
        p.next=None
        
        return head
