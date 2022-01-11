'''Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.'''
 

class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        
class MyLinkedList:

    def __init__(self):
        self.head=None
        
    def get(self, index: int) -> int:
        n=self.head
        
        i=0
        
        while index!=i:
            if n==None:
                return -1
            n=n.next
            i+=1
        if n==None:
            return -1
        return n.val

    def addAtHead(self, val: int) -> None:
        if self.head==None:
            n=Node(val)
            self.head=n
        else:
            n=Node(val)
            n.next=self.head
            self.head=n
        
        
    def addAtTail(self, val: int) -> None:
        if self.head==None:
            n=Node(val)
            self.head=n
        else:   
            n=self.head
            while n.next!=None:
                n=n.next

            m=Node(val)

            n.next=m
            m.next=None

    def addAtIndex(self, index: int, val: int) -> None:
        if self.head==None and index==0:
            n=Node(val)
            self.head=n
        elif index==0:
            n=Node(val)
            n.next=self.head
            self.head=n
        else:
            n=self.head
            self.head=n
            i=0

            while index-1!=i:
                if n==None:
                    break
                n=n.next
                i+=1
            if n!=None:
                m=Node(val)
                m.next=n.next
                n.next=m

    def deleteAtIndex(self, index: int) -> None:
        if index==0:
            self.head=self.head.next
        else:
            n=self.head
            m=n.next

            i=0

            while index-1!=i:
                if n==None or m==None:
                    break
                n=n.next
                m=m.next
                i+=1
            if n.next!=None:
                n.next=m.next
                m.next=None
        
    def traversal(self):
        n=self.head
        
        while n!=None:
            print(n.val)
            n=n.next
