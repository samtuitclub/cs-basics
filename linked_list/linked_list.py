class Node:
    def __init__(self):
        self.key = None
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def search(self, k):
        x = self.head
        while x != None and x.key != k:
            x = x.next
        return x

    def insert(self, x):
        temp = Node()
        temp.key = x
        temp.next = self.head
        if self.head != None:
            self.head.prev = temp
        self.head = temp

    def delete(self, x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev

