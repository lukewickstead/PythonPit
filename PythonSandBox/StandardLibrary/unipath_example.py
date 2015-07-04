# unipath_example.py
#
# unipath_example.py
#
# Object-oriented alternative to os/os.path/shutil

from time import gmtime

from unipath import Path


# Everything works around the Path class which can take any number of path name components which are concatenated to
# use the correct pathname separator.
#
# Path("/", "home", "lukey")        # An absolute path of /home/lukey
# Path("foo", "log.txt")            # A relative path of foo/log.txt
# Path(__file__)                    # The current running file
# Path()                            # Path(os.curdir)
# p = Path("")                      # An empty path

# Path
print("\n*** Path")
here = Path(__file__)
print(here)

# Path Properties
print("\n*** Path Properties")
print(here.components())  # A list of all the directories and the file as Path instances.
print(here.name)  # The file name
print(here.ext)  # The file extension
print(here.stem)  # The  file name without the extension

# Methods ( All return a Path instance )
print("\n*** Path Methods")
print(here.parent)  # The path without the file name
print(here.ancestor(5))  # Up x entities ( same as calling parent x times).
print(here.ancestor(3).child("PythonSandBox", "StandardLibrary"))  # Returns

print("\n*** Expand, Expand User and Expand Vars")
print(Path("~").expand_user())  # Expands ~ to a absolute path name
print(Path("$HOME").expand_vars())  # Expands system variables
print(Path("/home/luke/..").norm())  # Expands .. and . notation
print(Path("$HOME/..").expand())  # Expands system variables, ~ and also ..


# Expands system variable and ~. Will also normalise the path ( remove redundant
# .. . incorrect slashes and correct capitalisation on case sensitive file systems. Calls os.path.normpath

# File Attributes and permissions
print("\n*** File Attributes and permissions")
# noinspection PyArgumentList
print(here.atime())  # Last access time; seconds past epcoh
# noinspection PyArgumentList
print(here.ctime())  # Last permission or ownership modification; windows is creation time;
# noinspection PyArgumentList
print(here.isfile())  # Is a file; symbolic links are followed.
print(here.isdir())  # Is a directory; symbolic links are followed.
# noinspection PyArgumentList
print(here.islink())  # Is a symbolic link
# noinspection PyArgumentList
print(here.ismount())  # Is a mount point; ie the parent is on a different device.
# noinspection PyArgumentList
print(here.exists())  # File exists; symbolic links are followed.
# noinspection PyArgumentList
print(here.lexists())  # Same as exists but symbolic links are not followed.
# noinspection PyArgumentList
print(here.size())  # File size in bytes.
print(Path("/foo").isabsolute())  # Is absolute and not relative path

# Epoch?
print("\n*** gmtime")
print(gmtime(0))


# Stat and lstat
print("\n*** Stat and lstat")
print(here.stat())  # File stat object for size, permissions etc. Symbolic links are followed.
print(here.lstat())  # Same as stat  but symbolic links are not followed.
