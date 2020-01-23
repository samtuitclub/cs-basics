# Implementation of in place reverse of linked list


class Node:
    def __init__(self, value=None, next_n=None):
        self.value = value
        self.next = next_n


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        if self.head == None:
            self.head = Node(value=value)
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = Node(value=value)

    def reverse(self):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        prev_head = self.head
        self.head = current_node
        tmp_node = self.head
        while tmp_node != prev_head:
            current_node = prev_head
            while current_node.next != tmp_node:
                current_node = current_node.next
            tmp_node.next = current_node
            tmp_node = tmp_node.next
        prev_head.next = None

    def __str__(self):
        if self.head == None:
            return ""
        current_node = self.head
        res = ""
        while current_node != None:
            res += str(current_node.value) + "->"
            current_node = current_node.next
        return res + "NULL"


if __name__ == "__main__":
    a = LinkedList()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    a.insert(7)
    print(a)
    a.reverse()
    print(a)
