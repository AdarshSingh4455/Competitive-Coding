from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

print(queue[0]) # used to view the top element

print(queue.popleft()) # used to pop the element from starting with O(1) TC.

print(queue)

print(len(queue)) # return length of the queue...

print(not queue) # return false if queue is not empty