# references_and_immutable_objects_example.py
#
# References and Immutable Objects Example
#
#
# Variables in python are always references to objects.
# Objects can be mutable or immutable
#   Mutable (changeable) such as lists and classes can have their data changed
#       The following will create one list with two references.
#           one = (1, 2, 3)
#           two = one
#
#   Immutable (non changeable) such as strings can not be changed once created.
#       The following would create two string representations in memory.
#           foo = "A"
#           foo = "B"
#
# The following example shows seeing as variables are references to objects,
# a change to an object is shown in all references to it


name = 'Fred'
names = [name]
more_names = names
more_names.append('George')
name = 'Bill'

print("Name:", name)
print("Names:", names)
print("More Names:", more_names)

# The interesting thing here is that we append one name into names and more_names.
# We only have one list but it is referenced by two variables; so the list has two names in it.
# The variable name is added into the list and then later changed.
# As strings are immutable a new string is created and referenced by name.
# The string 'Fred' is no longer referenced by name but it is by the list.