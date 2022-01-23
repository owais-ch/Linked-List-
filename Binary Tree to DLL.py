'''Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right pointers in nodes are to be used as previous and next pointers respectively
in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of 
the DLL.'''

class Solution:
    def __init__(self):
        self.count=0
        self.head=None
        self.m=None
    def bToDLL(self,root):
        if root.left:
            self.bToDLL(root.left)
        
        if self.count==0:    
            self.m=Node(root.data)
            self.head=self.m
            self.count+=1
            
        else:
            hh=Node(root.data)
            self.m.right=hh
            hh.left=self.m
            self.m=self.m.right
            
        if root.right:
            self.bToDLL(root.right)
            
        return self.head
