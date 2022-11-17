from typing import Any

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def push(self, value:Any):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
    def append(self, value:Any):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next

        last.next=new_node
    def insert(self, value:Any, after:None):
        if after is None:
            print("Zły index")
            return
        new_node=Node(value)
        new_node.next=after.next
        after.next=new_node
    def pop(self):
        x = self.head
        if x is not None:
            self.head=x.next
            x = None
            return
    def remove_last(self):
        x = self.head
        while(x.next):
            prev=x
            x = x.next
        prev.next = None
    def remove(self, after:Node):
        if after is None:
            print("Error")
            return
        x = after.next.next
        after.next=x
    def print(self):
        x = self.head
        while(x):
            if x.next is None:
                print(x.data)
            else:
                print(x.data,"-> ", end="")
            x=x.next
    def len(self):
        dl = 0
        x = self.head
        while(x):
            dl+=1
            x = x.next
        return dl

class Stack:
    def __init__(self):
        self.storage=LinkedList()
    def push(self, element:Any):
        self.storage.push(element)
    def pop(self)->Any:
        self.storage.pop()
    def print(self):
        x = self.storage.head
        while(x):
            if x.next is None:
                print(x.data)
            else:
                print(x.data)
            x = x.next
    def len(self):
        dl = 0
        x = self.head
        while(x):
            dl+=1
            x = x.next
        return dl

class Queue:
    def __init__(self):
        self.storage = LinkedList()
    def peek(self):
        return self.storage.head.data
    def enqueue(self, element:Any)->None:
        self.storage.append(element)
    def print(self):
        x = self.storage.head
        while(x):
            if x.next is None:
                print(x.data)
            else:
                print(x.data, ", ", end="")
            x = x.next
    def dequeue(self) -> Any:
        self.storage.pop()
    def len(self):
        wynik = 0
        x = self.storage.head
        while (x):
            wynik += 1
            x = x.next
        return wynik
