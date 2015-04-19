# json_example.py
#
# JSON Example
#
# JSON or JavaScript Object Notation is an open standard format denoting key value pair entities.
#
# It is language independent.
#
# It is light weight and non describing alternative to XML. ( XML defines its structure )
#
# It's main use is a light weight communication between client and server; think AJAX !!

import json
from os import path

json_file_path = path.join('output', 'json.dump')

# Our raw data
data = {"numbers": [1, 2, 3, ],
        "written numbers": ['one', 'two', 'three'],
        "characters": ['a', 'b', 'c']}

print("*** The raw data:")
print(data)
print(type(data))

# dump an object into a json string
print("\n*** The json string:")
json_string = json.dumps(data)
print(json_string)
print(type(json_string))

# load a json string into an entity
decoded_data = json.loads(json_string)
print("\n*** The json string decoded:")
print(decoded_data)
print(type(decoded_data))


# json can be saved and loaded from an external file
print("\n*** Dump/Load from File:")

print("Dumping:", json_file_path)
with open(json_file_path, "w") as f:
    json.dump(data, f)

print("Loading:", json_file_path)
with open(json_file_path, "r") as f:
    loaded_json = json.load(f)
    print("\t", loaded_json)
    print("\t", type(loaded_json))

print("\n*** Pretty JSON Serialisation")
# sort_keys -   dictionary keys will be sorted
# indent    -   number of characters indent between nested elements within the list
# separators -  tuple of separation chars between list elements and keys
print(json.dumps(data, sort_keys=True, indent=2, separators=(',', ':')))