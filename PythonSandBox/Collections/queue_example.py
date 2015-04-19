# queue_example.py
#
# Queue Example
#
# First In First Out

from collections import deque

numbers = []

for x in range(10):
    numbers.append(x)

queue = deque(numbers)
print(queue)
print(type(queue))

# Remove from start of queue
print("\nRemove from start")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

# Remove from end of queue
print("\nRemove from end")
print(queue.pop())
print(queue.pop())
print(queue.pop())


