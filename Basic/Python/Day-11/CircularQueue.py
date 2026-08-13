class CircularQueue:

    def __init__(self,capacity):
        self.queue = [None]* capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, value):
        if self.is_full():
            return False

        self.rear = (self.rear + 1)% self.capacity
        self.queue[self.rear]=value
        self.size += 1

        return True

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.queue[self.front]
        self.queue[self.front]= None
        self.front = (self.front+1)% self.capacity
        self.size -= 1

        return value

    def peek(self):
        if self.is_empty():
            return None

        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def Size(self):
        return self.size

    def is_full(self):
        return self.size == self.capacity

    def show(self):
        return self.queue

    def empty_slots(self):
        if self.is_full():
            return False

        print(f"Yes...It has {self.capacity-self.size} empty slot.")


capacity = 5
cq = CircularQueue(capacity)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

print(cq.show())
print(cq.dequeue())
print(f"Size of the Circular Queue is: {cq.Size()}")
print(cq.show())
cq.empty_slots()

print(f"Enqueue operation is succesfull ? : {cq.enqueue(60)}")
print(cq.show())
print(f"Enqueue operation is succesfull ? : {cq.enqueue(70)}")

print(f"Size of the Circular Queue is: {cq.Size()}")
print(f"Circular queue is full : {cq.is_full()}")
print(f"Circular queue is empty : {cq.is_empty()}")