'''You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        n=l1
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        m=l2
        
        list2=[]
        
        while m!=None:
            list2.append(m.val)
            m=m.next
        
        number1=int(''.join(list(map(str,list1))))
        number2=int(''.join(list(map(str,list2))))
        
        number3=number1+number2
        if number3==0:
            head=ListNode(0)
            return head
        list4=[]
                    
        while number3>0:
            remainder=number3%10
            number3=number3//10
            list4.append(remainder)
                    
        list4.reverse()
        
        length=len(list4)
        
        h=ListNode(list4[0])
        head=h
        
        for i in range(1,length):
            mm=ListNode(list4[i])
            h.next=mm
            h=h.next
            
        return head
