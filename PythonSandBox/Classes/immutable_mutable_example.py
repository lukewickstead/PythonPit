# immutable_mutable_example.py
#
# Immutable Mutable Example
#
# *** IMMUTABLE VS. MUTABLE
#
# The concept of value and reference types is not present in python; instead we have immutable and mutable types.
#
# Immutable objects cannot have their state changes. Types include numbers, strings and tuples.
#
# Mutable objects can have their state changed. Types include dictionaries and lists.
#
# All data is considered an object and is assigned a unique id when it is created. It's type is defined at runtime and
# once set can never change, however it's state can be changed.
#
# The id() function can be used to get the id of an object.
# The type() function can be used to get the type of an object.

print("\nType & Object Id")
print('type("foo"): ', type("foo"))
print('id("foo"): ', id("foo"))

# Mutability vs. Creation; immutable objects appearing to be modified are actually creating new object instances
print("\nMutability vs. Creation")
one = 1
print(id(one))
one += 1
print(id(one))

# For Immutable objects with the same state or value; only one object is physically created.
print("\nImmutable objects with the same state")
print(id(1))
print(id(1))

a = 1
b = 1
print(id(a))
print(id(b))

# For mutable objects, multiple variables can point to the same object instance. The following will create one
#  list with two references:
one = [1, 2, 3]
two = one
one.append(4)
print("\nReferences the same object")
print(id(one), one)
print(id(two), two)


# *** MIXING IMMUTABLE & MUTABLE TYPES ***
# The following example shows seeing as variables are references to objects,
# a change to an object is shown in all references to it

name = 'Fred'
names = [name]
more_names = names
more_names.append('George')
name = 'Bill'

print("\nMixing Immutable and Mutable Types")

print("Name:", name)
print("Names:", names)
print("More Names:", more_names)

# The interesting thing here is that we append one name into names and more_names.
# We only have one list but it is referenced by two variables; so the list has two names in it.
# The variable name is added into the list and then later changed.
# As strings are immutable a new string is created and referenced by name.
# The string 'Fred' is no longer referenced by name but it is by the list.
