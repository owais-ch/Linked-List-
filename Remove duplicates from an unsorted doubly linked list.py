'''Given an unsorted doubly linked list containing n nodes. The problem is to remove duplicate nodes from the given list.'''

def remove_duplicates(head):
    n=head
    
    dict1=dict()
    
    w=None
    
    while n!=None:
        if n.data not in dict1:
            dict1[n.data]=1
            if w==None:
                w=n
                headw=n
            else:
                w.next=n
                temp=w
                w=w.next
                w.prev=temp
        n=n.next
    
    w.next=None
    
    return headw
