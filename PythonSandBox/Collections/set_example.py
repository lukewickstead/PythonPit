# set_example.py
#
# Set Example

# set() used to initialise
print("*** Initialisation")
numbers_bag = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
numbers_set = set(numbers_bag)

print(numbers_bag)
print(numbers_set)
print(type(numbers_set))


# Set Operations
set_one = {1, 2, 3, 4, 5, 6}
set_two = {5, 6, 7, 8}

print(set_one - set_two)  # Except: all in LHS but not in RHS. AKA Difference.
print(set_one | set_two)  # Or: all in LHS or RHS. AKA Union
print(set_one & set_two)  # And: all in LHS and RHS. AKA intersection
print(set_one ^ set_two)  # Logical OR: all in LHS or RHS but not both.


# Subset and SuperSet
# Subset: all elements in LHS are found within the RHS
# Superset: all elements in RHS are found within the LHS
print("\nSubset and Superset")
print({1, 2} <= {1, 2, 3})
print({1, 2, 3} >= {1, 2})