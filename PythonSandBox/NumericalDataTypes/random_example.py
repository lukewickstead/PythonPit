# random_example.py
#
# Random Example
#
# A module which allows functionality for randomness
#

from random import random, sample, randrange, randint, choice, uniform, shuffle

print("A random float:", random())  # no start, no stop
print("A random float within a range:", uniform(1, 10))  # start, stop
print("A random int:", randint(1, 99))  # start, stop
print("A random odd int:", randrange(1, 99, 2))  # start, stop, step/increment
print("A random choice:", choice('abcdefghi'))  # Random choice from an enumerable
print("A random sample", sample([1, 2, 3, 4, 5], 2))  # Any 2 elements from the list

letters = "a,b,c,d".split(',')
shuffle(letters)
print("Shuffled Letters:", letters)  # Shuffle an enumerable
