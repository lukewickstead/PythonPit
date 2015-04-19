# unipath_example.py
#
# unipath_example.py
#
# Object-oriented alternative to os/os.path/shutil

from unipath import Path

here = Path(__file__)

# Creation
print("Path(__file__):", here)

# Traversal
print("here.parent:", here.parent)
print("here.ancestor(1):", here.ancestor(1))
print("here.parent.child('unipath_example.py'):", here.parent.child("unipath_example.py"))
print("here.parent.child('unipath_example.py').stem:", here.parent.child("unipath_example.py").stem)
print("here.parent.child('unipath_example.py').ext:", here.parent.child("unipath_example.py").ext)

# Attributes
print("here.isdir():", here.isdir())
print("Path('Does Not Exist', 'No Such File').exists():", Path("Does Not Exist", "No Such File").exists())