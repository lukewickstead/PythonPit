# glob_example.py
#
# Glob Example
#
# Glob provides functionality for getting a list of files on a hard disk. It also supports regular expressions filters

import glob

print("*** Finding glob*.*")
for name in glob.glob('glob*.*'):
    print(name)

print("*** Finding *.txt")
for name in glob.glob('*.txt'):
    print(name)