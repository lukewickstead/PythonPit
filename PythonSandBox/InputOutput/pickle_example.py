# pickle_example.py
#
# Pickle Example
#
# Pickle is a python specific binary serialisation protocol
#
# cPickle is consumed automatically with Python 3 if it is available.
#

import pickle
from os import path

pickle_file = path.join('output', 'pickle.data')

# Our raw data
data = {"numbers": [1, 2, 3, ],
        "written numbers": ['one', 'two', 'three'],
        "characters": ['a', 'b', 'c']}

print("*** The raw data:")
print("\t", data)
print("\t", type(data))

# Serialisation
try:
    with open(pickle_file, "wb") as output_file:
        print("\nDumping to:", pickle_file)
        pickle.dump(data, file=output_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as pickle_error:
    print('Pickling error: ' + str(pickle_error))

# Deserialization
try:
    with open(pickle_file, "rb") as input_file:
        print("Loading from:", pickle_file)
        loaded_data = pickle.load(input_file)
        print("\t", loaded_data)
        print("\t", type(loaded_data))
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as pickle_error:
    print('Pickling error: ' + str(pickle_error))