from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSandBox.settings')

import django

django.setup()

from ..models import MultiTableBaseChild

names = {"George", "Morgan", "Luke"}
ages = {10, 20, 30}


def populate():
    for name, age in zip(names, ages):
        save_multi_table_base_child(name, age)


def print_data():
    for child in MultiTableBaseChild.objects.all():
        print(child)
        # The child has access to the fields contained within the parent table as if they are local
        # print(child.name, child.age)


def save_multi_table_base_child(name, age):
    return MultiTableBaseChild.objects.get_or_create(age=age, defaults={"name": name})[0]

# Execution
if __name__ == '__main__':
    populate()
    print_data()
