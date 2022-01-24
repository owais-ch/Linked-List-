'''Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 

Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].'''

class Solution:
    def splitListToParts(self, head, k):
        n=head
        
        i=0
        
        while n!=None:
            i+=1
            n=n.next
            
        num_elems=i
        
        list1=[]
        
        m=head
            
        while m!=None:
            list1.append(m.val)
            m=m.next
        
        if num_elems<=k:    
            list1.extend([None]*(k-num_elems))
            
            length=len(list1)
            
            list2=[]
            q=ListNode(list1[0])
            head=q
            
            if list1[0]==None:
                list2.append(list1[0])
            else:
                list2.append(q)
            
            for i in range(1,length):
                if list1[i]!=None:
                    hh=ListNode(list1[i])
                    list2.append(hh)
                else:
                    list2.append(list1[i])
                
            return list2
        
        else:
            numz=len(list1)//k
            num_elems=[numz for i in range(k)]
            remaining=len(list1)%k
            
            i=0
            
            while remaining>0:
                num_elems[i]+=1
                remaining-=1
                if i==k-1:
                    i=0
                else:
                    i+=1
                    
            m=ListNode(list1[0])
            head=m
            start=num_elems[0]
            
            for i in range(1,start):
                hh=ListNode(list1[i])
                m.next=hh
                m=m.next
            
            list3=[head]
            
            
            
            for i in range(1,k):
                m=ListNode(list1[start])
                head=m
                for j in range(start+1,start+num_elems[i]):
                    hh=ListNode(list1[j])
                    m.next=hh
                    m=m.next
                list3.append(head)
                start=start+num_elems[i]
                
            return list3
