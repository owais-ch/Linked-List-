
'''Given a binary tree and an integer K. Find the number of paths in the tree which have their sum equal to K.
A path may start from any node and end at any node in the downward direction.


Example 1:

Input:      
Tree = 
          1                               
        /   \                          
       2     3
K = 3
Output: 2
Explanation:
Path 1 : 1 + 2 = 3
Path 2 : only leaf node 3
'''

class Solution:
    def sumK(self,root,k):
        def root_node(root):
            nonlocal sum1,count1
            
            if root==None:
                return 0
                
            sum1+=root.data
            
            
                
            if sum1==k:
                count1+=1
            if sum1-k in dict1:
                count1+=dict1[sum1-k]
            #print(dict1)    
            if sum1 not in dict1:
                dict1[sum1]=1
            else:
                dict1[sum1]+=1
            if root_node(root.left) or root_node(root.right):
                return True
            
            dict1[sum1]-=1
            if dict1[sum1]==0:
                dict1.pop(sum1)
            sum1-=root.data
            
            return False
            
        sum1=0
        count1=0
        dict1=dict()
        
        root_node(root)
        
        return count1
