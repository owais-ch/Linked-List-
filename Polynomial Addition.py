'''Given two polynomial numbers represented by a linked list. The task is to complete the function addPolynomial() that adds these lists meaning adds the coefficients
who have the same variable powers.
Note:  Given polynomials are sorted in decreasing order of power.

Example 1:

Input:
LinkedList1:  (1,x2) 
LinkedList2:  (1,x3)
Output:
1x^3 + 1x^2
Explanation: Since, x2 and x3 both have
different powers as 2 and 3. So, their
coefficient can't be added up.'''

import numpy as np
class Solution:
    # return a linked list denoting the sum with decreasing value of power
    def addPolynomial(self, poly1, poly2):
        n=poly1
        dict1=dict()
        
        while n!=None:
            if n.power not in dict1:
                dict1[n.power]=[n.coef]
            else:
                dict1[n.power].append(n.coef)
            
            n=n.next
            
        m=poly2
        
        while m!=None:
            if m.power not in dict1:
                dict1[m.power]=[m.coef]
            else:
                dict1[m.power].append(m.coef)
            m=m.next
           
        for i in dict1:
            dict1[i]=np.sum(dict1[i])
        #print(dict1)
        list1=[[dict1[i],i] for i in dict1]
        list1.sort(key=lambda x:-x[1])        
        length=len(list1)
        
        q=node(list1[0][0],list1[0][1])
        head=q
        for i in range(1,length):
            hh=node(list1[i][0],list1[i][1])
            q.next=hh
            q=q.next
            
        q.next=None
        return head
