# raising_an_exception.py
#
# Raising An Exception

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(inst)
    print(inst.args)
