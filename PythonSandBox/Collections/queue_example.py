# queue_example.py
#
# Queue Example
#
# First In First Out

from collections import deque

numbers = list(range(10))
queue = deque(numbers)
print(queue)
print(type(queue))

# Remove from start of queue
print("\nRemove from start")
print(queue.popleft())
print(queue)

# Remove from end of queue
print("\nRemove from end")
print(queue.pop())
print(queue)

# Append to the end
print("\nAppend to the end")
queue.append(10)
print(queue)

# Append to the start
print("\nAppend to the start")
queue.appendleft(11)
print(queue)

# Append all elements from a collection to the end
print("\nExtend a collection")
queue.extend((12, 13, 14))
print(queue)

# Counts the number of occurrences of an element within the collection
print("\nCount the number of elements")
print(queue.count(12))

# Removes all elements.
print("\nRemove all elements")
queue.clear()
print(queue)
