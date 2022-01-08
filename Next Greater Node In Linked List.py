'''You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger 
value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, 
set answer[i] = 0.

Example 1:

Input: head = [2,1,5]
Output: [5,5,0]
Example 2:

Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]'''

class Solution:
    def nextLargerNodes(self, head):
        n=head
        if n.next==None:
            return [0]
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        stack=[list1[-1]]
        list2=[0]
        
        length=len(list1)
        
        j=1
        
        for i in range(-2,-length-1,-1):
            
            while stack!=[]:
                if list1[i]<stack[-1]:
                    list2.append(stack[-1])
                    break
                else:
                    stack.pop()
            
            if stack==[]:
                list2.append(0)
                stack.append(list1[i])
            else:
                stack=list1[i:][::-1]
            
            
        list2.reverse()
        
        return list2

