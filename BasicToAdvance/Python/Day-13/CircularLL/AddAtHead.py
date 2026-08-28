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

cll = CircularLinkedlist()
cll.addAtHead(10)
cll.addAtHead(15)
cll.addAtHead(20)

current = cll.head

while True:
    print(current.data," -> " , end =" ")
    current = current.next
    if current == cll.head:
        break