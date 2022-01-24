'''Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
 

Example 1:


Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]'''

import random
class Solution:

    def __init__(self, head):
        self.index=0
        self.head=head
        
    def traversal(self):
        n=self.head
        length=0
        
        while n!=None:
            length+=1
            n=n.next
            
        return length
    def getRandom(self):
        length=self.traversal()
        index=random.randint(0,length-1)
        n=self.head
        
        for i in range(index):
            n=n.next
        if n==None:
            return None
        return n.val
