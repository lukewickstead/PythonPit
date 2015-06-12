# timedelta_example.py
#
# TimeDelta Example
#

from datetime import datetime, timedelta


# Time Delta
print("\n*** Constructor")
# Only days, seconds and microseconds are stored internally, all other entities are converted
a_timedelta = timedelta(days=1, seconds=2, microseconds=3, milliseconds=0, minutes=0, hours=0, weeks=0)
print(a_timedelta)

print("\n*** Days, seconds, microseconds, total_seconds")
print(a_timedelta.days)
print(a_timedelta.seconds)
print(a_timedelta.microseconds)
print(a_timedelta.total_seconds())  # Seconds contained in days, second sand microseconds


# Min, Max, Resolution
print("\n*** Min, Max, Resolution")
print("Min = {0}, Max = {1}, Resolution = {2}".format(timedelta.min, timedelta.max, timedelta.resolution))

print("\n*** As String")
print(a_timedelta)
print(str(a_timedelta))
print(repr(a_timedelta))


# The timedelta can be used to
# We can subtract or add time deltas onto datetime objects
print("\n*** Operations")
today = datetime.now()
yesterday = datetime.now() - timedelta(days=1)
print("today - yesterday: ", today - yesterday)
print("(today - yesterday).seconds: ", (today - yesterday).total_seconds())
