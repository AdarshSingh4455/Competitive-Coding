class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:

    def insert_at_beginning(self, head, data):
        new_node = Node(data)
        new_node.next = head
        return new_node

    def insert_at_end(self, head, data):
        new_node = Node(data)

        if head is None:
            return new_node

        current = head

        while current.next is not None:
            current = current.next

        current.next = new_node
        return head


ll = LinkedList()

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head = ll.insert_at_beginning(head, 5)
print("After inserting at beginning:")
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
print()

head = ll.insert_at_end(head, 40)
print("After inserting at end:")
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
print()
