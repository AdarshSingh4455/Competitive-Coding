# Insertion in the middle of a singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertion_in_middle(head, value):
    # Insert a node containing `value` in the middle of the list.
    new_node = Node(value)

    if head is None:
        return new_node

    if head.next is None:
        head.next = new_node
        return head

    slow = head
    fast = head
    prev = None

    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Insert before the middle node
    if prev is None:
        new_node.next = head
        return new_node

    prev.next = new_node
    new_node.next = slow
    return head


head = Node(10)
b = Node(20)
c = Node(30)

head.next = b
b.next = c

head = insertion_in_middle(head, 25)

current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
