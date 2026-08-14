import heapq as hq

pq = []

hq.heappush(pq,(2,'Hello'))
hq.heappush(pq,(3,'Namaste'))
hq.heappush(pq,(1,'whatsup'))

print(pq)
print(hq.heappop(pq))
print(hq.heappop(pq))

print(pq)