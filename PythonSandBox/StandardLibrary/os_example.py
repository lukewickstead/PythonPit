# os_example.py
#
# OS Example
#
# Miscellaneous operating system interfaces
#
# See shutil for better file and directory management functionality

import os

print("os.name:", os.name)
print("os.uname:", os.uname())

print("os.path:", os.path)
print("os.environ")
for x in os.environ.items():
    print("\t\t{0} => {1}".format(x[0], x[1]))
    break

print("os.environ.get('HOME')", os.environ.get('HOME'))

print("os.getcwd:", os.getcwd())
os.chdir('/')
print("os.chdir('/')")
print("os.getcwd:", os.getcwd())

print("os.getegid:", os.getgid())  # User Group Id
print("os.getuid:", os.getuid())  # User Id
print("os.getgroups:", os.getgroups())  # User Groups

print('os.putenv("Fluffy", "Yes")')
os.putenv("Fluffy", "Yes")
print('os.getenv("Fluffy")', os.getenv("HOME"))


# Commented out due to potential destructive nature
# os.system("mkdir XXX")        # Run terminal command
# os.remove("\aDir")            # Remove directory