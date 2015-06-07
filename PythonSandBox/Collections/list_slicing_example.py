# list_slicing_example.py
#
# List Slicing Example
#
# Collections can be sliced; elements at a range or ordinal (index) positions can be accessed simultaneously
#

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slice; applicable for any indexed collection
print("*** Slicing ***")
print("numbers[0:3]:", numbers[0:3])    # Element at index 1 until < 3
print("numbers[8:]:", numbers[8:])      # Element at index 8 until the end
print("numbers[-3:]:", numbers[-3:])    # Elements from the third to last to the last
print("numbers[:]:", numbers[:])        # All elements (shallow copy)
print("0:len(numbers):1:", numbers[0:len(numbers):1])  # the same as above
print("numbers[::2]:", numbers[::2])    # Every other element
print("numbers[1::-2]:", numbers[::-2])  # Same as above.
print("numbers[len(numbers):0:-2]:", numbers[len(numbers):0:-2])  # Every other element backwards: same as above.


# Slice and Assign
print("\n\n*** Slice & Assign ***")

# Assign 99 and 100 to index 1 and 2
numbers[0:2] = [99, 100]
print("numbers[0:2] = [99, 100] =>", numbers)

# Remove range
numbers[0:2] = []
print("numbers[0:2] = [] =>", numbers)

# Clear all
numbers[:] = []
print("numbers[:] = [] =>", numbers)