# shutil_example.py
#
# Shutil Example
#
# Provides a high level interface for file and directory operations
#
# For more help:
#   dir(shutil)
#   help(shutil)
#
# Due to the destructive nature of this module most of the examples are commented out

import shutil

# Moving / Copying and Deleting
#   move("source_file.txt", "target_dir" )
#   copy("source_file.txt", "target_file.txt" )
#   copytree("source_dir", "target_dir")
#   rmtree("source")

# Archive
# Get the archive formats available
print(shutil.get_archive_formats())
# make_archive(archive_name, 'gztar', root_dir)
# unpack_archive(archive_name, "source_dir", "gztar" )

# Disk Space
print(shutil.disk_usage("/"))

# Which
print(shutil.which("python"))
print(shutil.which("python3"))


