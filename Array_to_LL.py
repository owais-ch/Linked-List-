'''
Array to Linked List
Given an array of integer arr. Your task is to construct the linked list from arr & return the head of the linked list.

Examples:

Input: arr = [1, 2, 3, 4, 5]
Output: LinkedList: 1->2->3->4->5
Explanation: Linked list for the given array will be
'''

class Solution:
    def constructLL(self, arr):
        n=None
        head=None
        for i in arr:
            if head==None:
                n=Node(i)
                head=n
            else:
                n.next=Node(i)
                n=n.next
                
        return head
