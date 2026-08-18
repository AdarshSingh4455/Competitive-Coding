class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_by_value(head,target):
    # to handle the empty linked list
    if head is None:
        return None
    # to handle the target of first element
    if target == head.data:
        return head.next
    current = head.next
    prev = head
    while current is not None:
        if current.data == target:
            prev.next = current.next
            return head
        prev = current
        current = current.next
    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

head = delete_by_value(head, 30)

current = head

while current is not None:
    print(current.data, end=" ")
    current = current.next