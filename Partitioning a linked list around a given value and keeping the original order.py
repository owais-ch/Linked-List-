'''Given a linked list and a value x, partition it such that all nodes less than x come first, then all nodes with a value equal to x, 
and finally nodes with a value greater than or equal to x. The original relative order of the nodes in each of the three partitions should be preserved. 
The partition must work in place.

Examples: 

Input : 1->4->3->2->5->2->3, 
        x = 3
Output: 1->2->2->3->3->4->5'''


def partitioning(head,x):
    n=head
    
    less=None
    equal=None
    great=None
    
    headl,heade,headg=None,None,None
    
    while n!=None:
        if n.data<x:
            if less==None:
                less=n
                headl=less
            else:
                less.next=n
                less=less.next
        elif n.data==x:
            if equal==None:
                equal=n
                heade=equal
            else:
                equal.next=n
                equal=equal.next
        else:
            if great==None:
                great=n
                headg=great
            else:
                great.next=n
                great=great.next
        n=n.next
        
    if headl!=None:
        if heade!=None:
            less.next=heade
            less=less.next
            if headg!=None:
                equal.next=headg
                equal=equal.next
                great.next=None
        if headg!=None:
                less.next=headg
                less=less.next
                great.next=None    
        return headl
    elif heade!=None:
        if headg!=None:
            less.next=headg
            less=less.next
            great.next=None 
        else:
            less.next=None
            
        return heade
    else:
        great.next=None
        return headg
