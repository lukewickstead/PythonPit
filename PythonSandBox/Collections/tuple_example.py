
# tuple_example.py
#
# Tuple Example
#
# Tuples are an immutable list; you can not edit the data once it bas been created.
#
# All non editing functionality of lists is available; slicing, indexing etc
#
# Tuples are faster than lists and should be used for constant data.
# An ideal contender for dictionary keys ( where all contained data is immutable )

from collections import namedtuple


tuple_one = 1, 2, 3
tuple_two = 1,

print(tuple_one)
print(tuple_two)

print("\n***Initialisation")
empty = ()
a_tuple = ('abcd', 786, 2.23, 'john', 70.2)
print(empty)
print(a_tuple)
print(type(a_tuple))

print("\n***Nested")
one = (1, 2, 3)
two = one, one
print(two)

# Tuples can be initialised by packing
print("\n*** Packing")
packed_tuple = 1, 2, 3  # packing
print(packed_tuple)
another = 1, (1, 2, 3)
print(packed_tuple)

print("\n*** Packing With One Element")
one_element = 'hello',  # note the trailing comma
print(one_element)
print(type(one_element))

print("\n*** Unpacking")
one, two, three, four = (1, 2, 3, 4)
print(one, two, three, four)


# Tuples can use all list style functionality as long as it does not edit the data
print("\n*** List Style Functionality")
print(a_tuple)              # Prints complete list
print(a_tuple[0])           # Prints first element of the list
print(a_tuple[1:3])         # Prints elements starting from 2nd till 3rd
print(a_tuple[2:])          # Prints elements starting from 3rd element
print(a_tuple * 2)          # Prints list two times
print(a_tuple + a_tuple)    # Prints concatenated tuples

print("\n*** Named Tuples")
Person = namedtuple("Person", ["name", "age"])
a_person = Person(name="Luke", age=36)

print(a_person)
print(type(a_person))
print(a_person.name)
print(a_person.age)

# a_person.age = 1 Data is still readonly. This results in a AttributeError exception being raised