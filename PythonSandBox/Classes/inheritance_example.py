# inheritance_example.py
#
# Inheritance Example


class Person:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def __str__(self):
        return '{0} is {1} years old'.format(self.Name, self.Age)


class Boy(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.Sex = "Boy"

    def __str__(self):
        return "{0} and is a {1}".format(super().__str__(), self.Sex)


a_person = Person("Luke", 36)
print(a_person)

a_boy = Boy("LukeyBoy", 36)
print(a_boy)

# True if is instance or instance of a class derived from
print("\nIsInstance:")
print("Is a_boy an instance of Boy?:", isinstance(a_boy, Boy))
print("Is a_boy an instance of Person?:", isinstance(a_boy, Person))
print("Is a_person an instance of Boy?:", isinstance(a_person, Boy))

print("\nIsSubClass:")
# Can not be called on an instance; has to be called on the class type.
print("Is Boy A SubClass of Boy?:", issubclass(Boy, Boy))
print("Is Boy A SubClass of Person?:", issubclass(Boy, Person))
print("Is Person A SubClass of Boy?:", issubclass(Person, Boy))
