'''Given a singly linked list: A0→A1→…→An-1→An, reorder it to: A0→An→A1→An-1→A2→An-2→…
For example: Given 1->2->3->4->5 its reorder is 1->5->2->4->3.

Note: It is recommended do this in-place without altering the nodes' values.

Example 1:

Input:
LinkedList: 1->2->3
Output: 1 3 2'''


def reorderList(self):
    if (self.head==None or self.head.next==None):
        return
    n=self.head
    
    list1=[]
    
    while n!=None:
        list1.append(n)
        n=n.next
        
    length=len(list1)
    
    i=0
    j=length-1
    
    while i<j:
        if i==0:
            p=list1[i]
            head=p
            q=list1[j]
            p.next=q
            p=p.next
        else:
            hh=list1[i]
            p.next=hh
            p=p.next
            hh=list1[j]
            p.next=hh
            p=p.next
            
        i+=1
        j-=1
    if length%2!=0:
        p.next=list1[length//2]
        p=p.next
    p.next=None
    return head
