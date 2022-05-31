'''Problem Statement
You have given a singly linked list and two integers 'N' and 'M'. Delete 'N' nodes after every 'M' node, or we can say more clearly that traverse the linked list such that you retain 'M' nodes then delete next 'N' nodes, continue the same till the end of the linked list.
Follow Up:
Try to solve this problem in O(N) time complexity and O(1) space complexity.
Input Format :
The first line of input contains the elements of the singly linked list separated by a single space and terminated by -1. Hence, -1 would never be a list element.

The second line contains the two single space-separated integers 'N' and 'M'.'''


def getListAfterDeleteOperation(head, n, m) :
    if head==None:
        return None
    q=head
    w=head
    head1=q
    count1=1
    count2=0
    while w!=None and w.next!=None:
        while count1<m and w!=None:
            w=w.next
            q.next=w
            q=q.next
            count1+=1
            
        while count2<n and w!=None:
            w=w.next
            count2+=1
        
        count1=0
        count2=0
    if q!=None:
        q.next=None        
    return head1
