import heapq as hq

class PriorityQueue:

    def __init__(self):
        self.items = []

    def hpush(self,value):
        return hq.heappush(self.items, value)

    def hpop(self):
        if not self.items:
            return False
        return hq.heappop(self.items)

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


queue = PriorityQueue()
queue.hpush(10)
queue.hpush(15)
queue.hpush(20)
print(queue.show())
print(queue.peek())
print(queue.hpop())
print(queue.peek())
print(queue.size())
print(queue.is_empty())
print(queue.show())