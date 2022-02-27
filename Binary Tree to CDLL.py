'''Given a Binary Tree of N edges. The task is to convert this to a Circular Doubly Linked List(CDLL) in-place. The left and right pointers in nodes are to be used
as previous and next pointers respectively in converted CDLL. The order of nodes in CDLL must be same as Inorder of the given Binary Tree. The first node of Inorder
traversal (left most node in BT) must be head node of the CDLL.

Example 1:

Input:
      1
    /   \
   3     2
Output:
3 1 2 
2 1 3
Explanation: After converting tree to CDLL
when CDLL is is traversed from head to
tail and then tail to head, elements
are displayed as in the output.'''

class Solution:
    
    #Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        def traversal(root):
            if root==None:
                return None
                
            if root.left:
                traversal(root.left)
                
            list1.append(root)
            
            if root.right:
                traversal(root.right)
                
        list1=[]
        
        traversal(root)
        
        length=len(list1)
        
        m=list1[0]
        m.left=None
        head=m
        
        for i in range(1,length):
            hh=list1[i]
            hh.left=m
            m.right=hh
            m=m.right
            
        m.right=head
        
        return head
