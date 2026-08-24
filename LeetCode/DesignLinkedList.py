class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index):
        current = self.head
        idx = 0

        while current:
            if idx == index:
                return current.val

            current = current.next
            idx += 1

        return -1

    def addAtHead(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def addAtIndex(self, index, val):
        if index < 0:
            return

        # Find current length
        length = 0
        current = self.head

        while current:
            length += 1
            current = current.next

        # Invalid index
        if index > length:
            return

        # Insert at beginning
        if index == 0:
            self.addAtHead(val)
            return

        # Insert at end
        if index == length:
            self.addAtTail(val)
            return

        # Insert in middle
        current = self.head
        idx = 0

        while idx < index - 1:
            current = current.next
            idx += 1

        new_node = Node(val)

        new_node.next = current.next
        current.next = new_node

    def deleteAtIndex(self, index):
        if self.head is None or index < 0:
            return

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        current = self.head
        prev = None
        idx = 0

        while current and idx < index:
            prev = current
            current = current.next
            idx += 1

        if current is None:
            return

        prev.next = current.next

        if current is self.tail:
            self.tail = prev


# # Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)