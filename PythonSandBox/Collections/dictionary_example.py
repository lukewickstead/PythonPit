# dictionary_example.py
#
# Dictionary Example

# {} is used to initialise
print("*** Initialisation")
dictionary_one = {}
print(type(dictionary_one))
print(dictionary_one)
print("Length: ", dictionary_one.__len__())

# KVP initialisation
print("\n*** KVP Initialisation")
dictionary_two = {'three': 3, 4: "four"}
print(dictionary_two)

# Assignment via key
print("\n*** Assignment via key")
dictionary_one[1] = "one"
dictionary_one["two"] = 2
print(dictionary_one)

# Reference via key
print("\n*** Reference via key")
print(dictionary_one[1])  # Element access by a key
print(dictionary_one["two"])  # Element access by a key


# Named key dictionary
print("\n*** Named key dictionary")
dictionary_named = dict(a="one", b="two", c="three", d="four")
print(dictionary_named)
print(dictionary_named['a'])

print("\n*** Accessing Key and Values collections")
print("dictionary_one.keys():", dictionary_named.keys())
print("dictionary_one.values():", dictionary_named.values())

print("\n*** Looping Dictionary")
for k in dictionary_named:
    print(k)

print("\n*** Looping Dictionary.Items")
for kvp in dictionary_named.items():
    print(kvp)


# Tuples can be used as a key if they contain only immutable objects; strings, numbers, or tuples
# If a tuple contains any mutable object either directly or indirectly, it cannot be used as a key

dict_with_tuples = {('a', 'b'): 'ab', ('a', 'c'): 'ac', ('a', 'c'): 'ac'}

print("\n*** Tuples as Keys")
print(dict_with_tuples)
print(('a', 'b') in dict_with_tuples.keys())