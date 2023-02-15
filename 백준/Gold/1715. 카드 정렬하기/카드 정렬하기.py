from queue import PriorityQueue
pq=PriorityQueue()

for _ in range(int(input())):
    pq.put(int(input()))
    
s=0
while pq.qsize() > 1:
    data1=pq.get()
    data2=pq.get()
    data=data1+data2
    s+=data
    pq.put(data)
print(s)