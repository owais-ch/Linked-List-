'''Given a Singly Linked List which has data members sorted in ascending order. Construct a Balanced Binary Search Tree which has same data members as the given Linked List.
Note: There might be nodes with same value.

Example 1:

Input:
Linked List: 1->2->3->4->5->6->7
Output:
4 2 1 3 6 5 7
Explanation :
The BST formed using elements of the 
linked list is,
        4
      /   \
     2     6
   /  \   / \
  1   3  5   7  
Hence, preorder traversal of this 
tree is 4 2 1 3 6 5 7'''


class Solution:
    def sortedListToBST(self, head):
        n=head
        list1=[]
        
        while n!=None:
            list1.append(n.data)
            n=n.next
            
        def buildBST(arr):
            if not arr:
                return None
                
            mid=len(arr)//2
            
            root=TNode(arr[mid])
            
            root.left=buildBST(arr[:mid])
            root.right=buildBST(arr[mid+1:])
            
            return root
            
        return buildBST(list1)
