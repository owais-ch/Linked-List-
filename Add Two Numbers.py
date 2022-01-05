'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        n=l1
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        list1.reverse()
        number1=int(''.join(list(map(str,list1))))
                   
        m=l2
        
        list2=[]
        
        while m!=None:
            list2.append(m.val)
            m=m.next
                   
        list2.reverse()
                   
        number2=int(''.join(list(map(str,list2))))
                    
        number3=list(map(int,list(str(number1+number2))))
        number3.reverse()
        length=len(number3)
        
        hh=l1
        l1=hh
        hh.val=number3[0]
        
        for i in range(1,length):
            mm=ListNode(number3[i])
            hh.next=mm
            hh=hh.next
            
        return l1
