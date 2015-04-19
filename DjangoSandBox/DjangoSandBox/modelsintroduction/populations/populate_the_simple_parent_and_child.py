from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSandBox.settings')

import django

django.setup()

from modelsintroduction.models import TheSimpleChild, TheSimpleParent


def populate():
    for number in range(20):
        child = save_child("C{0}".format(number))
        save_parent("P{0}".format(number), child)


def print_data():
    for a_parent in TheSimpleParent.objects.all():
        print("{0} --> {1}".format(a_parent, a_parent.child))


def save_parent(name_value, child):
    return TheSimpleParent.objects.get_or_create(name=name_value, child=child)[0]


def save_child(name_value):
    return TheSimpleChild.objects.get_or_create(name=name_value)[0]

# Execution
if __name__ == '__main__':
    print("Populating TheSimpleParent, TheSimpleChild")
    populate()
    print_data()