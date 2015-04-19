# binary_file_io_example.py
#
# Binary File I/O Example
#
# All access to files are made via the file class and the open method,
#
# a_file = open("A-File-T0-Read.txt", "rb")
#
# r:    Readonly (Default)
# w:    Write (Overwrite Existing)
# a:    Write Append (Opened at end of file for appendage)
# r+:   Read/Write
#
# Defaults as UTF-8 (text). Specify b for binary

from os import path

binary_file = path.join('output', 'binary.bin')

data = ["Hello", "There"]

with open(binary_file, 'wb') as f:
    for a_number in "\n".join(data):
        f.write(bytes(a_number, 'UTF-8'))

with open(binary_file, 'rb') as f:
    print(f.read().decode('UTF-8'))