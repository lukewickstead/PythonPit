# set_example.py
#
# Set Example

# set() used to initialise
print("*** Initialisation")
numbers_bag = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
numbers_set = set(numbers_bag)

print(numbers_set)
print(type(numbers_set))

# Set Operations
set_one = {1, 2, 3, 4, 5, 6}
set_two = {5, 6, 7, 8}

print(type(set_one))
print(set_one, "except", set_two, "=", set_one - set_two)  # in one except in two
print(set_one, "or", set_two, "=", set_one | set_two)  # in one except in two
print(set_one, "and", set_two, "=", set_one & set_two)  # in one except in two
print(set_one, "either but not both", set_two, "=", set_one ^ set_two)  # in one except in two

# Subset and SuperSet
print((1, 2, 3), "is a subset of", (1, 2, 3, 4), (1, 2, 3) <= (1, 2, 3, 4))
print((1, 2, 3), "is a super set of", (1, 2, 3), (1, 2, 3, 4) >= (1, 2, 3))