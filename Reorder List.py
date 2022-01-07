'''You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]'''

class Solution:
    def reorderList(self, head):
        n=head
        
        nodes=[]
        
        while n!=None:
            nodes.append(n)
            n=n.next
            
        head=nodes[0]
        
        length=len(nodes)
        
        i=0
        j=length-1
        
        while i<j:
            nodes[i].next=nodes[j]
            nodes[j].next=nodes[i+1]
            i+=1
            j-=1
        if length%2!=0:
            nodes[j].next=None
        else:
            nodes[j+1].next=None 

