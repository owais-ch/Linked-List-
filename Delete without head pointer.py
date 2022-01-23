'''You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes. The task is to delete the node. Pointer/ reference to head node is not given. 
Note: No head reference is given to you. It is guaranteed that the node to be deleted is not a tail node in the linked list.

Example 1:

Input:
N = 2
value[] = {1,2}
node = 1
Output: 2'''


class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        n=curr_node
        curr_node=n
        while n.next!=None:
            n.val=n.next.val
            if n.next.next==None:
                n.next=None
                return curr_node
            n=n.next
