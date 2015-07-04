# os_example.py
#
# OS Example
#
# Miscellaneous operating system interfaces
#
# https://docs.python.org/3.4/library/os.html

import os

# Name and uname
print("\n*** Name and uname")
print(os.name)  # OS Name
print(os.uname())  # OS Uname

# Current Working Directory and Change Directory
print("\n*** cdw and chdir")
print(os.getcwd())  # Current Working Directory (CWD)
os.chdir('/')  # Change CWD
print(os.getcwd())

# Users and Groups
print("\n*** UserGouprId, UserId, UserGroups")
print(os.getgid())  # UserGroupId of running process
print(os.getuid())  # UserId of running process
print(os.getgroups())  # List of User Groups

# System Variables
print("\n*** System Variables")
print(os.getenv("HOME"))  # Get System variable
os.putenv("Fluffy", "Yes")  # Set System Variable
print(os.getenv('Fluffy'))

# Access to most terminal commands.
# os.mkdir("\foo")
# os.rmdir("\foo")
# os.system("mkdir XXX")        # Run terminal command
