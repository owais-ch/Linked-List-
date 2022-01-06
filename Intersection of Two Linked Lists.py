'''Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.'''


class Solution:
    def getIntersectionNode(self, headA, headB):
        n=headA
        m=headB
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
        
        list2=[]
        
        while m!=None:
            list2.append(m.val)
            m=m.next
            
        length_1=len(list1)
        length_2=len(list2)
        
        i=-1
        
        count=0
        
        while i>=-length_1 and i>=-length_2:
            if list1[i]==list2[i]:
                count+=1
            else:
                break
            i=i-1
                
        target_1=length_1-count
        target_2=length_2-count
        
        n=headA
        m=headB
        
        
        for i in range(target_1):
            n=n.next
            
        for i in range(target_2):
            m=m.next
            
        if length_2<length_1:
            for i in range(target_2,length_2):
                if m==n:
                    return m
                else:
                    m=m.next
                    n=n.next
        elif length_1<=length_2:
            for i in range(target_1,length_1):
                if m==n:
                    print(m.val)
                    return m
                else:
                    m=m.next
                    n=n.next
                
        return None
