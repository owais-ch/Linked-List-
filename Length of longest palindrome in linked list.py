'''Given a linked list, the task is to complete the function maxPalindrome() which returns an integer denoting  the length of the longest palindrome list that exist 
in the given linked list.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains an integer N
denoting the size of the linked list . Then in the next line are N space separated values of the given linked list.

Output:
For each test case output will be the required max length of the palindrome present in the given linked list.'''

def maxPalindrome(head):
    n=head
    list1=[]
    
    while n!=None:
        list1.append(n.data)
        n=n.next
        
    length=len(list1)
    
    maximum=1
    
    for i in range(length-1):
        for j in range(i+1,length):
            if list1[i:j+1]==list1[i:j+1][::-1]:
                
                count=j+1-i
                maximum=max(maximum,count)
                
    return maximum
    
