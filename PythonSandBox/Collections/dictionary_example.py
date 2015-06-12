# dictionary_example.py
#
# Dictionary Example

# A collection of elements indexed on a unique identifier or key.

# {} or dict() is used to create an instance.
print("*** Initialisation")
dictionary_one = {}
print(type(dictionary_one), dictionary_one, len(dictionary_one))
dictionary_one = dict()
print(type(dictionary_one), dictionary_one, len(dictionary_one))


# Initialising with data requires specifying the key and the element
print("\n*** KVP Initialisation")
print({'three': 3, 4: "four"})

# Assignment is made via the key. They keys can be any immutable data instance, and they can even be of mixed type.
print("\n*** Assignment via key")
dictionary_one[1] = "one"
dictionary_one["two"] = 2
print(dictionary_one)

# Element reference is made via the key
print("\n*** Reference via key")
dictionary_one = {1: 'one', 'two': 2}
print(dictionary_one[1])
print(dictionary_one["two"])
print("1 in dictionary_one: ", 1 in dictionary_one)

# Named key dictionary
print("\n*** Named key dictionary")
dictionary_named = dict(a="one", b="two", c="three", d="four")
print(dictionary_named)
print(dictionary_named['a'])

print("\n*** Accessing Key and Values collections")
dictionary_one = {1: 'one', 'two': 2}
print("dictionary_one.keys():", dictionary_one.keys())
print("dictionary_one.values():", dictionary_one.values())

print("\n*** Looping Dictionary")
for k in dictionary_one:
    print(k)

print("\n*** Looping Dictionary.Items")
for k, v in dictionary_one.items():
    print(k, v)

# Keys can be anything which is immutable. Tuples can be used as a key if they contain only immutable objects; strings,
# numbers, or tuples. If a tuple contains any mutable object either directly or indirectly, it cannot be used as a key

print("\n*** Tuples as Keys")
dict_with_tuples = {('a', 'b'): 'ab', ('a', 'c'): 'ac', ('a', 'c'): 'ac'}
print(dict_with_tuples)
print(('a', 'b') in dict_with_tuples.keys())
