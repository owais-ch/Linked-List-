'''Given the head of a singly linked list, return true if it is a palindrome.

Example 1:

Input: head = [1,2,2,1]
Output: true'''

class Solution:
    def isPalindrome(self, head):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        if list1==list1[::-1]:
            return True
        else:
            return False
        
