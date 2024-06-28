'''Given a singly linked list of size N, and an integer K. You need to swap the Kth node from the beginning and Kth node from the end of the linked list.
Swap the nodes through the links. Do not change the content of the nodes.

 

Example 1:

Input:
N = 4,  K = 1
value[] = {1,2,3,4}
Output: 1
Explanation: Here K = 1, hence after
swapping the 1st node from the beginning
and end thenew list will be 4 2 3 1.'''


def swapkthnode(head,num,k):
    def length_ll(head):
        length=1
        
        fast=head
        
        while fast!=None and fast.next!=None:
            if fast.next.next!=None:
                length+=2
            elif fast.next!=None:
                length+=1
            fast=fast.next.next
            
        return length
        
    length=length_ll(head)
    
    if k>length or length==1:
        return head
    elif k==length and length!=2:
        k=1
    elif length==2:
        n=head
        m=head.next
        m.next=n
        n.next=None
        head=m
        return head
    
        
    if k==1:
        ntemp1=head.next
        ptemp1=None
        first=head
        
        i=0
        n=head
        
        while i<length-k-1:
            if i+2<length-k-1:
                n=n.next.next
                i+=2
            else:
                n=n.next
                i+=1
        
            
        ptemp2=n
        ntemp2=None
        second=n.next
        
        first.next=second.next
        second.next=ntemp1
        ptemp2.next=first
        head=second
        first.next=None
    else:
        length=length_ll(head)
        i=0
        n=head
        
        while i<k-1:
            ptemp1=n
            n=n.next
            i+=1
            
        first=n    
        ntemp1=first.next
        
        n=head
        i=0
        while i<length-k-1:
            if i+2<length-k-1:
                n=n.next.next
                i+=2
            else:
                n=n.next
                i+=1
             
        ptemp2=n
        second=n.next
        ntemp2=second.next
        
        if first==second:
            return head
            
        if first.next==second:
            ptemp1.next=second
            first.next=ntemp2
            second.next=first
            return head
        elif second.next==first:
            ptemp2.next=first
            second.next=ntemp1
            first.next=second
            return head
            
        #print(first.data,second.data,'wwww')
        ### swapping
        
        first.next=second.next
        second.next=ntemp1
        ptemp2.next=first
        ptemp1.next=second
        
    return head
