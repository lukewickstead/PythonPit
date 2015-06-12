# shutil_example.py
#
# Shutil Example
#
# Provides a high level interface when working with files or collection of files.
#
# Due to the destructive nature of this module most of the examples are commented out

from shutil import move, copy, copytree, rmtree, get_archive_formats, make_archive, unpack_archive, disk_usage, which

# Moving / Copying and Deleting
# move("source_file.txt", "target_dir" )
# copy("source_file.txt", "target_file.txt" )
# copytree("source_dir", "target_dir")

# rmtree("source")

# Archive
# Get the archive formats available
print(get_archive_formats())
# make_archive(archive_name, 'gztar', root_dir)
# unpack_archive(archive_name, "source_dir", "gztar" )

# Disk Space
print(disk_usage("/"))

# Which
print(which("python"))
print(which("python3"))


