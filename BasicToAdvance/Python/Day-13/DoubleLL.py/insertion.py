class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b

b.prev = a
b.next = c

c.prev = b
c.next = d

d.prev = c

tail = d

current = tail

while current is not None:
    print(current.data, end=" ")
    current = current.prev