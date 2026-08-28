class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def addAtTail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return

        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

cll = CircularLinkedList()
cll.addAtTail(5)
cll.addAtTail(10)
cll.addAtTail(20)
cll.addAtTail(30)

current = cll.head
while True:
    print(current.data)
    current = current.next
    if current == cll.head:
        break