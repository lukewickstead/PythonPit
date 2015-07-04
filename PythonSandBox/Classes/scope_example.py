# scope_example.py
#
# Scope Example

# Variables can be local, nonlocal or global.
#
# Global variables exist at the top level ( not inside a class or method )
#
# Local:
#       Variables are by default local when inside a method.
#       They shadow a variable with the same name in an outer scope ( calling method, class etc ).
#       Changes to a local variable does not affect any variables which they shadow
#
# Global:
#       The global keyword is used to import a global variable,
#       It allows a variable to be used and set inside a method
#       It only imports global variables and not outer scope variables which are not global (inside a calling method)
#
# Nonlocal:
#       Similar to global but will import variable which are in an outer scope but are either global or not global


def print_scope_msg(a_msg):
    print("Inside scope_test:", a_msg)


msg = "Initial"


def scope_test():

    # noinspection PyShadowingNames
    def local_test():
        # msg is local. Changes are only existing inside the method
        msg = "local"
        print("Inside local_test():", msg)

    def nonlocal_test():
        # msg is non local. This allows the msg inside scope_test() to be imported and edited
        nonlocal msg
        msg = "nonlocal"
        print("Inside nonlocal_test:", msg)

    def global_test():
        # msg is global. This allows the msg inside global but not scope_test() to be imported and edited
        # Changes to msg affect the global msg but not the scope_test (it skips it)
        global msg
        msg = "global"
        print("Inside global_test: ", msg)

    msg = "scope"

    local_test()
    print_scope_msg(msg)

    nonlocal_test()
    print_scope_msg(msg)

    global_test()
    print_scope_msg(msg)

scope_test()
print("Inside global:", msg)
