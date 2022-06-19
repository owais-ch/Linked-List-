'''Problem Statement

Given a linked list containing a series of numbers that are separated by ‘0’. You need to find the sum of the series and replace the series’s elements with its sum.

Sample Input 1 :
2
2 5 7 0 3 4 0 -1
1 2 3 0 -1
Sample Output 1 :
14 7
6
'''

def replaceWithSum(head):
    n=head
    count=0
    m=head
    while m!=None:
        if m.data!=0:
            head1=m
            break
        m=m.next
    m=head1
    n=m
    sum1=0
    
    while n!=None:
        if n.data!=0:
            
            if sum1==0:
                q=n
            sum1+=n.data
        elif n.data==0:
            m.data=sum1
            if n.next!=None:
                m=m.next
            else:
                m.next=None
            sum1=0
            count+=1
        n=n.next
    if sum1!=0 and count>0:
        m.data=q.data
        
        m.next=q.next
        m=m.next
    
    
    return head1
