# class_example.py
#
# Class Example
#
#
# - Classes in Python feel little more than giving functions scope; this becomes
# apparent when referencing variables which are external to the class or class method.
#
# - Classes are dynamic; they are created at run time and can even be changed dynamically.
#
# - All member functions are virtual by default; they can be overridden by inheriting classes
#
# - All member functions are public by default; unless explicitly defined as private

# The class keyword is used to define the scope of a class:
# - All subsequent and indented functions are assigned to that class
# - The method __init__ is the constructor and is called implicitly when creating an instance
# - Instance variables are created and assigned via the self keyword
# - The method __str__ is called when outputting the instance to the terminal with the print() method


class Person():
    IsHuman = "Yes"

    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def __str__(self):
        return '{0} is {1} years old. Is human = {2}'.format(self.Name, self.Age, self.IsHuman)

# Creating an instance of a class is used with the class name; passing in any required parameters:

print("\n*** Classes")
a_person = Person("Luke", 36)
print(a_person)

# IsInstance can be used to see if a class instance is an instance of a class
print("Is {0} a Person?: {1}".format(a_person.Name, isinstance(a_person, Person)))

print("\n*** Classes are dynamic")
# Classes are dynamic and generated during runtime; here we add IsCool onto a class instance
a_person.IsCool = "In a quirky way"
print("Is {0} a cool?: {1}".format(a_person.Name, a_person.IsCool))

# Subsequent classes won't respond to the IsCool instance method which was added onto another class
a_person = Person("Luke", 36)

if hasattr(a_person, 'IsCool'):
    print("Is {0} a cool?: {1}".format(a_person.Name, a_person.IsCool))
else:
    print("{0} does not respond to IsCool".format(a_person.Name))

# Class Variables. Though shared, immutable objects appear to be instance variables, mutable objects are shared.
# It is considered bad practice to use class variables

print("\n*** Class Variables")


class ClassVariable():
    AnInt = 1
    AList = []

    def __str__(self):
        return "AnInt = {0}, AList = {1}".format(self.AnInt, self.AList)


one = ClassVariable()
two = ClassVariable()
one.AnInt += 1
one.AList.append("Item-1")

print(one)
print(two)

two.AList = []
print(one)
print(two)
