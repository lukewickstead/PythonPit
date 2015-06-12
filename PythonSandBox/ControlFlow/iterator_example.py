# iterator_example.py
#
# Iterator Example
#
# Any objects which defined __iter__ and __next__ can be loop over with a for loop
#
# Alternatively any method using the yield keyword can also be used in a for loop

# iter class can be used to iter over a collection
print("*** Iterators Respond to Next")
it = iter("abc")
print(next(it))
print(next(it))

print("\n*** A Simple Iterator Class")
# Simply write __iter__ and __next__


class MyRangeClass:
    def __init__(self, start, stop):
        self.start = start
        self.index = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.stop:
            raise StopIteration
        self.index += 1
        return self.index


for x in MyRangeClass(1, 3):
    print(x)

print("\n*** Yield Keyword")
# Generates __iter()__ and __next__ automatically


def count_down(count):
    while count > 0:
        yield count
        count -= 1


for x in count_down(3):
    print(x)
