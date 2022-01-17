'''Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

Example 1:

Input:
N = 3
value[] = {1,3,4}'''

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        n=head
        
        dict1=dict()
        
        while n!=None:
            dict1[n]=1
            n=n.next
            
            if n in dict1:
                return True
        return False
