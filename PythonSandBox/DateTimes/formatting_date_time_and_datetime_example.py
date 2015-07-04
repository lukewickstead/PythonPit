# formatting_date_time_and_datetime_example.py
#
# Formatting date, time and datetime classes
#
# The following part templates are provided. They can be used with date,time and datetime where applicable.
#
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


from datetime import datetime, date

# Formatting Strings
print("m-%d-%y: ", date.today().strftime("%m-%d-%y"))
print("%d %b %Y %X:", datetime.now().strftime("%d %b %Y %X"))


# isoformat
print("\n***isoformat")
print(datetime.today().isoformat())
print(date.today().isoformat())

# ctime
print("\n***ctime")
print(datetime.today().ctime())
print(date.today().ctime())
