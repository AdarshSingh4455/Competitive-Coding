from collections import deque

queue = deque()

queue.append(10)
queue.append(15)
queue.append(21)

print(queue.popleft())

print(queue)
