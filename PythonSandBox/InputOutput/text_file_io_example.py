# text_file_io_example.py
#
# Text File I/O Example
#
# All access to files are made via the file class and the open method,
#
#
# a_file = open("A-File-T0-Read.txt", "r")
#
# r:    Readonly (Default)
# w:    Write (Overwrite Existing)
# a:    Write Append (Opened at end of file for appendage)
# r+:   Read/Write
#
# Defaults as UTF-8 (text). Specify b for binary

from os import path

text_file = path.join('output', 'output.txt')

data = ["This is a list of strings", "which need to be saved", "into a file"]

# Writing to a file
print("\nSaving to:", text_file)
with open(text_file, "w") as f:
    for a_line in data:
        f.write(a_line)
        f.write("\n")

# Read all lines at the same time
print("\nReading all lines from:", text_file)
with open(text_file, "r") as f:
    print(f.readlines())

# Though line but line access can be read with read() and readline(); the file is an enumerator
print("\nReading line by line from:", text_file)
with open(text_file, "r") as f:
    for a_line in f:
        print(a_line, end='')  # The file has new line chars also print adds one on by default


# List can be used to parse a file
print("\nRead with list():", text_file)
with open(text_file, "r") as f:
    print(list(f))
    print(list(f))
    f.seek(0)
    print(list(f))

# List Seek can be used to move the current marker location through out the file
# Pass required position as a byte; 9 is the start
# Tell can be used to get the current position in bytes
print("\nRead with seek:", text_file)
with open(text_file, "r") as f:
    print(list(f))
    print(list(f))
    f.seek(0)
    print(list(f))