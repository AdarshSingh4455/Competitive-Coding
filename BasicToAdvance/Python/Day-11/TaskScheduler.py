import heapq

tasks = [
    (2,0,"Hello"),
    (3,1,"Namaste"),
    (2,2,"KemChho"),
    (1,3,"Hey..Whatsup"),
]

pq = []
for task in tasks:
    heapq.heappush(pq,task)

def process_tasks(pq):

    result = []
    while pq:
        _, _, value = heapq.heappop(pq)
        result.append(value)

    return result

def peek_priority(pq):
    if not pq:
        return None
    
    _, _, value = pq[0]
    return value


print(peek_priority(pq))
x = process_tasks(pq)
print(x)