'''You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.

Example 1:

Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.'''

class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        n=list1
        list1=n
        
        i=0
        
        arr1=[]
        arr2=[]
        
        while n!=None:
            if i<a:
                arr1.append(n)
                
            elif a<=i<=b:
                pass
            else:
                arr2.append(n)
            n=n.next    
            i+=1
            
        n=arr1[0]
        head=n
        
        for i in range(1,len(arr1)):
            n=n.next
            
        m=list2
        
        while m!=None:
            n.next=m
            n=n.next
            m=m.next
            
        for i in range(len(arr2)):
            n.next=arr2[i]
            n=n.next
            
        return head
