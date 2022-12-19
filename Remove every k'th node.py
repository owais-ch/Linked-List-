'''Given a singly linked list, your task is to remove every kth node from the linked list.

Input:
The first line of input contains number of test cases T. Then T test cases follow. Every test case contains 3 lines. First line of every test case contains an integer
N denoting the size of the linked list . The second line contains N space separated values of the linked list. The third line contains an integer K.

Output:
Output for each test case will be space separated values of the nodes of the new transformed linked list.'''

def deleteK(head, k):
    n=head
    if k==1:
        return None
    count=0
    
    while n!=None:
        count+=1
        if count==k-1 and n.next!=None:
            n.next=n.next.next
            count=0
        n=n.next    
    return head
