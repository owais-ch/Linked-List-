'''Given a linked list, return the node where the cycle begins. If there is no cycle, return null.'''

class Solution:
    def detectCycle(self, head):
        n=head

        dict1=dict()

        while n!=None:
            dict1[n]=1
            if n.next in dict1:
                return n.next

            n=n.next

        return None
