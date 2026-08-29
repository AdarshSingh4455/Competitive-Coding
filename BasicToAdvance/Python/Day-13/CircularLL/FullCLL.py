class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # -------------------------
    # Add at Head
    # -------------------------
    def addAtHead(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return

        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node

    # -------------------------
    # Add at Tail
    # -------------------------
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

    # -------------------------
    # Add at Index
    # -------------------------
    def addAtIndex(self, data, index):

        size = self.sizeOfLL()

        if index < 0 or index > size:
            return

        if index == 0:
            self.addAtHead(data)
            return

        if index == size:
            self.addAtTail(data)
            return

        new_node = Node(data)

        current = self.head.next
        prev = self.head
        idx = 1

        while current != self.head:

            if idx == index:
                new_node.next = current
                prev.next = new_node
                return

            prev = current
            current = current.next
            idx += 1

    # -------------------------
    # Traverse
    # -------------------------
    def traverse(self):

        if self.head is None:
            print("List is Empty.")
            return

        current = self.head

        while current.next != self.head:
            print(current.data, " -> ", end="")
            current = current.next

        print(current.data)

    # -------------------------
    # Size
    # -------------------------
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

    # -------------------------
    # Delete at Index
    # -------------------------
    def deleteAtIndex(self, index):

        size = self.sizeOfLL()

        if index < 0 or index >= size:
            return

        # Only one node
        if self.head == self.tail:

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

                # Delete tail
                if current == self.tail:
                    self.tail = prev

                self.tail.next = self.head
                return

            prev = current
            current = current.next
            idx += 1

    # Search index of Node
def searchNode(self, data):
    if self.head is None:
        return -1

    current = self.head
    idx = 0

    while True:
        if current.data == data:
            return idx

        current = current.next
        idx += 1

        if current == self.head:
            break

    return -1


# ==========================================
# Testing
# ==========================================

cll = CircularLinkedList()

cll.addAtHead(10)
cll.addAtHead(15)
cll.addAtHead(20)

cll.addAtTail(30)
cll.addAtTail(40)

print("Initial List:")
cll.traverse()

print("Size:", cll.sizeOfLL())


cll.addAtIndex(25, 3)

print("\nAfter inserting 25 at index 3:")
cll.traverse()

print("Size:", cll.sizeOfLL())


cll.deleteAtIndex(3)

print("\nAfter deleting index 3:")
cll.traverse()

print("Size:", cll.sizeOfLL())


cll.deleteAtIndex(0)

print("\nAfter deleting head:")
cll.traverse()

print("Size:", cll.sizeOfLL())

x =cll.searchNode(30)
if x >= 0:
    print("Element found at index: ", x)
else:
    print("Sorry! Element Not Found.")