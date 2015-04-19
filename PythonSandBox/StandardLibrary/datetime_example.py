# datetime_example.py
#
# Date Time Example

import datetime

# Contains the following types (classes)

# datetime.date: contains day, month and year
# datetime.time: contains hours, minutes and seconds etc.
# datetime.datetime: contains day, month, year, hours, minutes, seconds and tzinfo
# datetime.timedelta: time difference between two dates/times
# datetime.tzinfo: time zone information
# datetime.timezone: with a parent of tzinfo allows off setting from UTC

# Date
print("***Date")
print("datetime.date.now(): ", datetime.date.today())
print("datetime.date.now().day: ",  str(datetime.date.today().day))
print("datetime.date.now().month: ",  str(datetime.date.today().month))
print("datetime.date.now().year: ",  str(datetime.date.today().year))

# Dates can be constructed by components
print("datetime.date(1978, 10, 25).year", datetime.date(1978, 10, 25).year)


# Date Time
print("\n***Date Time")
print("datetime.datetime.now(): ", datetime.datetime.now())
print("datetime.datetime.now().day: ",  str(datetime.datetime.now().day))
print("datetime.datetime.now().month: ",  str(datetime.datetime.now().month))
print("datetime.datetime.now().year: ",  str(datetime.datetime.now().year))
print("datetime.datetime.now().hour: ",  str(datetime.datetime.now().hour))
print("datetime.datetime.now().minute: ",  str(datetime.datetime.now().minute))


# Time Delta
print("\n*** Time Delta")

print("datetime.timedelta(days=10):", datetime.timedelta(days=10))
print("datetime.timedelta(days=10).seconds:", datetime.timedelta(days=10).seconds)

# Differencing Dates
today = datetime.datetime.now()
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
print("today - yesterday: ", today - yesterday)
print("(today - yesterday).seconds: ", (today - yesterday).seconds)

# Formatting Strings
print("\n*** Formatting Date Ties")
print("m-%d-%y: ", datetime.date.today().strftime("%m-%d-%y"))
print("%d %b %Y:", datetime.date.today().strftime("%d %b %Y"))
print("%A/%B/%Y:", datetime.date.today().strftime("%A/%B/%Y"))


# Code	Example                 Description
# %a	Mon                     Name of day short
# %A	Monday                  Name of day
# %w	0                       Day of week as integral. Sunday - Saturday = 0 - 6
# %d	25                      Day of the month
# %b	Jan                     Name of month short
# %B	January                 Name of month
# %m	1                       Month (0-12)
# %y	79                      Short year ( last two digits)
# %Y	1978                    Year ( as 4 digits)
# %H	18                      Hour as integral of 24 hour clock
# %I	6                       Hour as integral of 12 hour clock
# %p	AM                      AM/PM
# %M	30                      Minute as integral
# %S	30                      Second as integral
# %f	989898                  Microsecond as integral
# %z	                        UTC offset (form +HHMM or -HHMM)
# %Z	                        Time zone name
# %j	213                     Day of the year
# %U	10                      Week number of the year ( Sunday as the first day of the week)
# %W	10                      Week number of the year (Monday as the first day of the week)
# %c	01/02/2014 12:30:55     Locale formatted date time
# %x	01/02/2014              Locale formatted date
# %X    12:30:55                Locale formatted time
