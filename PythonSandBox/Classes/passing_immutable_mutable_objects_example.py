# by_reference_by_value_example.py
#
# By Reference or By Value?
#
#
# Neither; arguments are passed by assignment in Python; a reference to the object is created.
#
# In .NET this is pass by value; a copy of the reference is passed where all objects are by reference.
#
# .NET Value types can not be changed so their state is modified outside of a function.
#
# .NET Reference types can be modified via methods but reassigning a new object to the reference does not change the
# object being pointed to outside; as a copy of the reference and not the reference is passed in.
#
# In Python:
#
# 01: You can change a mutable object; the changes are visible outside the method.
# 02  Changing a immutable object actually creates a new object instance, the change is not visible outside the method.
# 03: You can assign a new mutable object but it does not affect the value outside the method
# 04: You can assign a new immutable object but it does not affect the value outside the method


def append_value(a_data, to_input):
    a_data.extend(to_input)
    print("Inside append_value:", a_data)


mutable_data = []
print("*** Modifying a mutable object")
print("Before append_value:", mutable_data)
append_value(mutable_data, (1, 2, 3))
print("After append_value:", mutable_data)


def increment(an_int):
    an_int += 1
    print("Inside increment:", an_int)


data = 1
print("\n*** Modifying an immutable object")
print("Before increment:", data)
increment(data)
print("After increment:", data)


#  02: You can assign a new mutable object but it does not affect the value outside the method
def assign_value(a_data, to_assign):
    a_data = to_assign
    print("Inside append_value:", a_data)


mutable_data_two = []
print("\n\n *** Assignment - Mutable")
print("Before assign_value:", mutable_data_two)
assign_value(mutable_data_two, [1, 2, 3])
print("After assign_value:", mutable_data_two)

#  03: You can assign a new immutable object but it does not affect the value outside the method
immutable_data = "old value"
print("\n\n *** Assignment - Immutable")
print("Before assign_value:", immutable_data)
assign_value(immutable_data, "new value")
print("After assign_value:", immutable_data)
