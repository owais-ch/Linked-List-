'''Given a linked list L of N nodes, sorted in ascending order based on the absolute values of its data,i.e. negative values are considered as positive ones.
Sort the linked list according to the actual values, consider negative numbers as negative and positive number as positive.


Example 1:

Input: 
List: 1, -2, -3, 4, -5
Output: 
List: -5, -3, -2, 1, 4'''


def sortList(head):
    n=head
    list1=[]
    
    while n!=None:
        list1.append(n.data)
        n=n.next
        
    list1.sort()
    
    n=head
    head=n
    
    count=0
    while n!=None:
        n.data=list1[count]
        n=n.next
        count+=1
        
    return  head
