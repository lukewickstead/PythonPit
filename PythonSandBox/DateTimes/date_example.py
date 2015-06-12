# date_example.py
#
# Date Example
#
# datetime.date class provides an object representing a date.

from datetime import date


# Today
print("\n***today()")
today = date.today()
print("date.now(): ", today)

# Min / Max / Resolution
print("\nMin, Max, Resolution")
# noinspection PyUnresolvedReferences
print("Min = {0}, Max = {1}, Resolution = {2}".format(date.min, date.max, date.resolution))

# Date Components:
print("\n***Day.Month.Year")
print("{0}-{1}-{2}".format(today.day, today.month, today.year))

# Dates can be constructed by components
print("\n***Constructor")
print(date(1978, 10, 25))

# Replace
print("\n***Replace")
print(today.replace(1, 2, 3))

# Day Of Week
# weekday: Monday (0) - Sunday (6)
# iso weekday: Monday (1) - Sunday(7)
print("\n***Day of Week")
print(today.weekday())
print(today.isoweekday())

# Difference between two days
print("\n***Difference between two days")
print(today.replace(2016) - today)
