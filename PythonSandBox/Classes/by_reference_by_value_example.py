# by_reference_by_value_example.py
#
# By Reference or By Value?
#
#
# Neither; arguments are passed by assignment in Python; a reference to the object is created.
#
# In .NET this is pass by value; a copy of the item (vlaue types) / reference (reference types) is passed in.
#
# Value types can not be changed so their state is modified outside of a function.
#
# Reference types can be modified via methods but reassigning a new object t the reference does not change the object
# being pointed to outside; as a copy of the reference and not the reference is passed in.
#
# In Python:
#
#  01: You can change a mutable object;  the changes are visible outside the method.
#  02: You can assign a new mutable object but it does not affect the value outside the method
#  03: You can assign a new immutable object but it does not affect the value outside the method


#  01: You can change a mutable object
def append_value(data, to_input):
    data.extend(to_input)
    print("Inside append_value:", data)

mutable_data = []
print("*** Modifying a mutable object")
print("Before append_value:", mutable_data)
append_value(mutable_data, (1, 2, 3))
print("After append_value:", mutable_data)


#  02: You can assign a new mutable object but it does not affect the value outside the method
def assign_value(data, to_assign):
    data = to_assign
    print("Inside append_value:", data)

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