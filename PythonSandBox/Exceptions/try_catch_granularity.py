# try_catch_granularity.py
#
# Try Catch Granularity
#
# An exception is caught if it is the same type, or has the defined type in it's ancestry (inherits from it)

# noinspection PyBroadException
try:
    f = open('foo.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as err:
    print("IOError: {0}".format(err))
except ValueError as err:
    print("ValueError: {0}".format(err))
except Exception as err:
    print("Exception: {0}".format(err))
except:
    print("Won't ever execute due to the except condition above")

