'''Given elements as nodes of the two linked lists. The task is to multiply these two linked lists, say L1 and L2. 

Note: The output could be large take modulo 109+7.'''

def multiplyTwoList(head1, head2):
    n=head1
    
    list1=[]
    
    while n!=None:
        list1.append(n.data)
        n=n.next
        
    number1=int(''.join(list(map(str,list1))))
    
    m=head2
    
    list2=[]
    
    while m!=None:
        list2.append(m.data)
        m=m.next
        
    number2=int(''.join(list(map(str,list2))))
    
    return (number1*number2)%MOD
