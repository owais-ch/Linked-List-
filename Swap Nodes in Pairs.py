'''Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]'''

class Solution:
    def swapPairs(self, head):
        n=head
        head=n
        
        if n==None:
            return None
        elif n.next==None:
            return n
        else:
            m=n.next
            
            i=0
            while m!=None:
                if i==0:
                    n.next=m.next
                    m.next=n
                else:
                    n.next=m.next
                    m.next=n
                    q.next=m
                
                
                if i==0:
                    head=m
                if n.next==None or m.next==None:
                    return head
                
                q=n
                n=n.next
                m=n.next
                i+=1
            return head
