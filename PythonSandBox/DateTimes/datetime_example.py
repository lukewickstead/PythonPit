# datetime_example.py
#
# Date Time Example
#
# The datetime class combines functionality the functionality and state of the date and time classes
#

from datetime import datetime


# Now
print("\n***Today, Now, UTCNow")
print(datetime.today())
print(datetime.now())
print(datetime.utcnow())


# Range
print("\n***Min, Max, Resolution")
print("Min = {0}, Max = {1}, Resolution = {2}".format(datetime.min, datetime.max, datetime.resolution))


# Date Time
now = datetime.now()
print("\n***Day, Month, Year, Hour, Minute, Second")
print("{0}-{1}-{2} {3}:{4}:{5}".format(now.day, now.month, now.year, now.hour, now.minute, now.second))


# Constructor
print("\n***Constructor")
print(datetime(2001, 2, 3, 4, 5, 6))


# Replace
print("\n***Replace")
print(datetime.today().replace(1, 2, 3, 4, 5, 6, 7))

# Difference
print("\n***Difference between two dates")
print(datetime.now().replace(year=2016) - datetime.now())
