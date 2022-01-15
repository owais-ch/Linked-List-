'''Given a linked list, delete N nodes after skipping M nodes of a linked list until the last of the linked list.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of elements in the linked
list and next M and N respectively space separated. The last line contains the elements of the linked list.'''

class Solution:
    def skipMdeleteN(self, head, M, N):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n)
            n=n.next
            
        length=len(list1)  
        
        list2=[]
        count=0
        i=0
        while i<length:
            if count<M:
                list2.append(list1[i])
                count+=1
                i+=1
            else:
                count=0
                i+=N
                
        
        length2=len(list2)
        
        q=list2[0]
        head=q
        for i in range(1,length2):
            hh=list2[i]
            q.next=hh
            q=q.next
        q.next=None    
        return head
