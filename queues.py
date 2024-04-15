# Implementing using list

queue = []
queue.append('plane')
queue.append('lorry')
queue.append('bus')
queue.append('car')
queue.append('motorcycle')
queue.append('bicycle')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)


# Implementing using collections.deque

from collections import deque
q = deque()
q.append('apple')
q.append('banana')
q.append('dragon fruit')
q.append('dragon fruit')
q.append('kiwi')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
 
print("\nQueue after removing elements")
print(q)


# Implementation using queue.Queue

from queue import Queue
q = Queue(maxsize = 4)
print(q.qsize()) 
q.put('blouse')
q.put('shirt')
q.put('vest')
q.put('trouser')
print("\nFull: ", q.full())  #checks if the queue is full
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty()) #its false because i have only dequed 3 elements and left one
print("Full: ", q.full())  #its false because the size was 4



