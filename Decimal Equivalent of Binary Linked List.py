'''Given a singly linked list of 0s and 1s, the task is to find its decimal equivalent. Decimal Value of an empty linked list is considered as 0.

Since the answer can be very large, answer modulo 1000000007 should be printed.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains 

Output:
The function should return should decimal equivalent modulo 1000000007.'''

def decimalValue(head):
    MOD=10**9+7
    
    n=head
    list1=[]
    
    while n!=None:
        list1.append(n.data)
        n=n.next
        
    list1.reverse()
    
    length=len(list1)
    
    list1=[list1[i]*2**i for i in range(length)]
    
    sum1=sum(list1)
    
    return sum1%MOD
