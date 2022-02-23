'''Given a singly linked list containing N nodes. Modify the value of first half nodes such that 1st nodes new value is equal to the last nodes value minus first nodes 
current value, 2nd nodes new value is equal to the second last nodes value minus 2nd nodes current value, likewise for first half nodes. Replace the second half nodes with 
the first half nodes with initial values of first half nodes. If n is odd then the value of the middle node remains unchanged.
Note: Input in the linked list is like new node will be entered at the head position (1st position).'''

class Solution:
    #Function to reverse a linked list.
    def modifyTheList(self, head):
        n=head
        list1=[]
        
        while n!=None:
            list1.append(n.data)
            n=n.next
            
        length=len(list1)
        
        i=0;j=length-1
        
        while i<j:
            temp=list1[i]
            list1[i]=list1[j]-list1[i]
            list1[j]=temp
            i+=1
            j-=1
          
        m=Node(list1[0])
        head=m
        for i in range(1,length):
            hh=Node(list1[i])
            m.next=hh
            m=m.next
            
        return head
