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

        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node

    def addAtTail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return

        self.tail.next = new_node
        new_node.next = self.head
        self.tail = new_node

    def traverse(self):
        if self.head is None:
            print("List is an Empty.")
            return

        current = self.head
        while current.next != self.head:
            print(current.data, " -> ", end=" ")
            current = current.next
        print(current.data)

    def sizeOfLL(self):
        size = 0
        if self.head is None:
            return size

        current = self.head
        while True:
            size += 1
            current = current.next
            if current == self.head:
                break
        return size

    def deleteAtIndex(self, index):
        if self.head is None or index < 0:
            return

        # Only one node
        if self.head == self.tail:
            if index == 0:
                self.head = None
                self.tail = None
            return

        # Delete head
        if index == 0:
            self.head = self.head.next
            self.tail.next = self.head
            return

        current = self.head.next
        prev = self.head
        idx = 1

        while current != self.head:

            if idx == index:
                prev.next = current.next

                # If deleting tail
                if current is self.tail:
                    self.tail = prev

                self.tail.next = self.head
                return

            prev = current
            current = current.next
            idx += 1

cll = CircularLinkedlist()
cll.addAtHead(10)
cll.addAtHead(15)
cll.addAtHead(20)
cll.addAtTail(30)
cll.addAtTail(40)

cll.traverse()
print("Size of Circular Linked List : ", cll.sizeOfLL())
cll.deleteAtIndex(3)
cll.traverse()
print("Size of Circular Linked List after deletion of a node : ", cll.sizeOfLL())
cll.deleteAtIndex(0)
cll.traverse()
print("Size of Circular Linked List after deleting two nodes : ", cll.sizeOfLL())