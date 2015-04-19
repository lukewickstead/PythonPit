# timeit_example.py
#
# Timeit Example
#
# timeit provides some timer style functionality when running code

import timeit


def function_to_time(max_value):

    start = 0

    for count in range(max_value):
        start = start ** max_value


def run_timeit_by_lambda():

    t = timeit.Timer(lambda: function_to_time(100))

    for number in [100, 200, 300]:
        print("{0}: {1}".format(number, t.timeit(number=number)))


def run_timeit_by_string():

    for number in [100, 200, 300]:
        print("{0}: {1}".format(number, timeit.timeit('"-".join(str(n) for n in range(100))', number=number)))

print("*** Running Time it via lambda")
run_timeit_by_lambda()

print("\n*** Running Time it via string")
run_timeit_by_string()