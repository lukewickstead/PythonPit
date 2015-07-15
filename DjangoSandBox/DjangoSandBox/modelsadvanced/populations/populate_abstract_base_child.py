from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSandBox.settings')

import django

django.setup()

from ..models import AbstractBaseChild

names = {"George", "Morgan", "Luke"}
ages = {10, 20, 30}


def populate():
    for name, age in zip(names, ages):
        save_abstract_base_child(name, age)


def print_data():
    for child in AbstractBaseChild.objects.all():
        print(child)


def save_abstract_base_child(name, age):
    return AbstractBaseChild.objects.get_or_create(age=age, defaults={"name": name})[0]


# Execution
if __name__ == '__main__':
    populate()
    print_data()
