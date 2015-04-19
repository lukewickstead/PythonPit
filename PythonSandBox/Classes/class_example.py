# class_example.py
#
# Class Example
#
# Classes are dynamic; they are created at run time. They can be changed dynamically at runtime.
# All member functions are virtual; they can be overridden
# All member functions are public (unless defined private)


class Person():
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def __str__(self):
        return '{0} is {1} years old'.format(self.Name, self.Age)

a_person = Person("Luke", 36)
print(a_person)

# IsInstance is used to see if a class instance is an instance of a class
print("Is {0} a Person?: {1}".format(a_person.Name, isinstance(a_person, Person)))

# Classes are dynamic and generated during runtime; here we add IsCool onto a class instance
a_person.IsCool = "In a quirky way"
print("Is {0} a cool?: {1}".format(a_person.Name, a_person.IsCool))

# Subsequent classes won't respond to the IsCool instance method which was added onto another class
a_person = Person("Luke", 36)

if hasattr(a_person, 'IsCool'):
    print("Is {0} a cool?: {1}".format(a_person.Name, a_person.IsCool))
else:
    print("{0} does not respond to IsCool".format(a_person.Name))
