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

# Writing all lines to a file
print("\nSaving all lines to:", text_file)
with open(text_file, "w") as f:
    f.writelines(data)

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


# List Comprehensions
print("\nList comprehensions to read all lines into an array:", text_file)
lines = [line.rstrip('\n') for line in open(text_file)]
print(lines)


# List can be used to parse a file
print("\nRead with list():", text_file)
with open(text_file, "r") as f:
    print(list(f))

# Seek can be used to move the current marker throughout the file.
# The position is defined as the number of bytes from the start of the file. 0 is the very start.
# Tell can be used to get the current position in bytes
print("\nRead with seek:", text_file)
with open(text_file, "r") as f:
    print("Tell: ", f.tell())
    contents = list(f)
    print("Tell: ", f.tell())
    f.seek(0)
    print("Tell: ", f.tell())
