from collections import deque

class Queue:

    def __init__(self):
        self.items = deque()

    def enqueue(self,value):
        return self.items.append(value)

    def dequeue(self):
        if not self.items:
            return None

        return self.items.popleft()

    def peek(self):
        if not self.items:
            return None

        return self.items[0]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not self.items

    def show(self):
        return self.items


queue = Queue()
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)
print(queue.show())
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.size())
print(queue.is_empty())
print(queue.show())