'''Given a singly linked list of size N containing only English Alphabets. Your task is to complete the function arrangeC&V()
, that arranges the consonants and vowel nodes of the list it in such a way that all the vowels nodes come before the consonants while maintaining the order of their arrival.'''

class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        n=head
        list1=[]
        while n!=None:
            list1.append(n.data)
            n=n.next
        list2=[]
        list3=[]
        for i in list1:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                list2.append(i)
            else:
                list3.append(i)
                
        list4=list2+list3
        length=len(list4)
        m=Node(list4[0])
        head=m
        for i in range(1,length):
            hh=Node(list4[i])
            m.next=hh
            m=m.next
            
        return head
