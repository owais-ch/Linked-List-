'''Given a Linked List, an integer k and an element, add that element at the kth position of the linked list.

Example
List: 1→3→4→7
k: 2
Element: 5
Result: 1→5→3→4→7'''

class Solution:
    def addAtkthElement(self, head, k, newElement) -> ListNode:
        if k==1:
            n=newElement
            n.next=head
            head=n
            return head
        i=1
        n=head
        head=n
        while k!=i+1:
            i+=1
            n=n.next

        m=newElement
        m.next=n.next
        n.next=m

        return head
