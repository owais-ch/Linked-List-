'''Given a linked list of size N. The task is to complete the function countNodesinLoop() that checks whether a given Linked List contains 
a loop or not and if the loop is present then return the count of nodes in a loop or else return 0. C is the position of the node to which the last node is connected.
If it is 0 then no loop.'''


from collections import OrderedDict
#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    n=head
    
    dict1=OrderedDict()
    
    count=0
    
    while n!=None:
        dict1[n]=1
        n=n.next
        count+=1
        
        if n in dict1:
            return count-list(dict1.keys()).index(n)
        
    return 0
