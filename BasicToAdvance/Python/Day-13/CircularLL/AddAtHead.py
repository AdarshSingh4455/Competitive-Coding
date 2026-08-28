class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedlist:

    def __init__(self):
        self.head = None
        self.tail = None

    def addAtHead(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            self.tail = new_node
            return
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node