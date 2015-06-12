# time_example.py
#
# Time Example

import time

# Time is seconds or ticks since 12:00am, January 1, 1970
print("\n***Time")
print(time.time())

print("\n***Local Time")
print(time.localtime(time.time()))

# The above returns a struct_time which is a tuple with named elements in the following format

# Index	|   Attribute  |   Description  |   Range
# 0	    |   tm_year	    |   Year            |   Any int
# 1	    |   tm_mon	    |   Month           |   1 to 12
# 2	    |   tm_mday	    |   Day of month    |   1 to 31
# 3	    |   tm_hour	    |   Hour            |   0 to 23
# 4	    |   tm_min	    |   Minutes         |   0 to 59
# 5	    |   tm_sec	    |   Seconds         |   0 to 61 where 60/61 are leap-seconds
# 6	    |   tm_wday	    |   Day of  week    |   0 to 6 where 0 is Monday
# 7	    |   tm_yday	    |   Day of year     |   1 to 366 (Julian day)
# 8	    |   tm_isdst	|   Daylight saving |   1=y, 0=n, -1=library determines DST


print("\n***ASC Time")
print(time.asctime(time.localtime(time.time())))
