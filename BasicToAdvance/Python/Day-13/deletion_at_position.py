class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_at_position(head,position):
    # to handle the empty linked list
    if head is None:
        return None
    
    # to handle the target of first element
    if position == 0:
        return head.next
    
    current = head.next
    prev = head
    count = 1

    while current is not None:
        if count == position:
            prev.next = current.next
            return head
        
        prev = current
        current = current.next
        count += 1

    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

head = delete_at_position(head, 3)

current = head

while current is not None:
    print(current.data, end=" ")
    current = current.next