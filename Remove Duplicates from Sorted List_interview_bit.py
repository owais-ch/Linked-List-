'''Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,

Given 1->1->2, return 1->2.

Given 1->1->2->3->3, return 1->2->3.'''


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, head):
        n=head
        
        while n!=None:
            if n.next==None:
                    break
            if n.val==n.next.val:
                n.next=n.next.next
            else:
                n=n.next
                
        return head
