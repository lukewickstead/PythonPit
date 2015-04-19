# rethrowing_an_exception.py
#
# Rethrowing An Exception

try:
    f = open('foo.txt')
    s = f.readline()
    i = int(s.strip())
except:
    print("Caught!!")
    raise

print("This won't print!!!")
