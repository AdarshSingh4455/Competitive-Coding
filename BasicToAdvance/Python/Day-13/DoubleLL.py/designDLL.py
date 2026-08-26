class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertionAtbeginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertionAtEnd(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def deletion(self,current):
        if current == self.head and current == self.tail:
            self.head = None
            self.tail = None
        elif current == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif current == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False