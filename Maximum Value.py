'''Given a binary tree, find the largest value in each level.


Example 1:

Input:
        1
       / \
      2   3 
Output:
1 3
Explanation:
At 0 level, values of nodes are {1}
                 Maximum value is 1
At 1 level, values of nodes are {2,3}
                Maximum value is 3
'''

class Solution:
    def maximumValue(self,node):
        def traversal(root,level):
            if root==None:
                return None
                
            if level not in dict1:
                dict1[level]=root.data
            else:
                dict1[level]=max(dict1[level],root.data)
                
            if root.left:
                traversal(root.left,level+1)
                
            if root.right:
                traversal(root.right,level+1)
                
        dict1=dict()
        
        traversal(root,0)
        
        list1=sorted(list(dict1.items()),key=lambda x:x[0])
        
        return list(map(lambda x:x[1],list1))
