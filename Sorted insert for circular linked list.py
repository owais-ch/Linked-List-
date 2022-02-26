'''Given a sorted circular linked list, the task is to insert a new node in this circular list so that it remains a sorted circular linked list.

Example 1:

Input:
LinkedList = 1->2->4
(the first and last node is connected,
i.e. 4 --> 1)
data = 2
Output: 1 2 2 4'''

class Solution:
    def sortedInsert(self, head, data):
        n=head
        head=n
        if n.data>data:
            while n.next!=head:
                n=n.next
                
            m=Node(data)
            n.next=m
            m.next=head
            head=m
            
            return head
        else:
            while n.next.data<=data:
                n=n.next
            m=Node(data)
            m.next=n.next
            n.next=m
            
            return head
