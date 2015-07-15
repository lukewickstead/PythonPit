from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSandBox.settings')

import django

django.setup()

from ..models import Child, Parent

parent_names = ("Luke", "Dave", "Angus", "Bob", "Jim")
child_names = ({"Junior", "Mark"}, {"Sport", "Jim", "Simon", "Carl", "Erik"}, {"Randy", "Bob"}, {"Sophie"}, {None})


def populate():
    for parent_name, parent_child_names in zip(parent_names, child_names):
        a_parent = save_parent(parent_name)
        for child_name in parent_child_names:
            save_child(child_name, a_parent)


def print_data():
    for aParent in Parent.objects.all():
        print("{0} --> {1}".format(aParent, aParent.child_set.all()))


def save_parent(name):
    return Parent.objects.get_or_create(name=name)[0]


def save_child(name, a_parent):
    if name is None:
        return

    return Child.objects.get_or_create(name=name, defaults={'parent': a_parent})[0]


# Execution
if __name__ == '__main__':
    populate()
    print_data()
