'''Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
Note: The flattened list will be printed using the bottom pointer instead of next pointer.'''

def flatten(root):
    n=root
    m=root
    
    list1=[]
    
    while n!=None:
        list1.append(n.data)
        m=m.bottom
        while m!=None:
            list1.append(m.data)
            m=m.bottom
            
        n=n.next
        m=n
    list1.sort()    
    length=len(list1)
    
    q=Node(list1[0])
    head=q
    
    for i in range(1,length):
        hh=Node(list1[i])
        q.bottom=hh
        q=q.bottom
      
    return head
