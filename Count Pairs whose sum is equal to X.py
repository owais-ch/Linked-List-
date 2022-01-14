'''Given two linked list of size N1 and N2 respectively of distinct elements, your task is to complete the function countPairs(), which returns the count
of all pairs from both lists whose sum is equal to the given value X.
Note: The 2 numbers of a pair should be parts of different lists.

Example 1:

Input:
L1 = 1->2->3->4->5->6
L2 = 11->12->13
X = 15
Output: 3
Explanation: There are 3 pairs that
add up to 15 : (4,11) , (3,12) and (2,13)'''


from collections import Counter

class Solution:
    def countPair(self,h1,h2,n1,n2,x):
        
        n=h1
        
        list1=[]
        
        while n!=None:
            list1.append(n.data)
            n=n.next
        list1.sort()    
        m=h2
        
        list2=[]
        
        while m!=None:
            list2.append(m.data)
            m=m.next
        list2.sort()    
        count=0
        
        dict1=Counter(list2)
        
        for i in range(n1):
            if x-list1[i] in dict1:
                count+=1
                    
        return count
