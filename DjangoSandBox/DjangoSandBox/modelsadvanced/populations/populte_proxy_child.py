from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSandBox.settings')

import django

django.setup()

from ..models import ProxyChild

names = {"George", "Morgan", "Luke"}


def populate():
    for name in names:
        save_multi_table_base_child(name)


def print_data():
    for child in ProxyChild.objects.all():
        print(child)


def save_multi_table_base_child(name):
    return ProxyChild.objects.get_or_create(name=name)[0]


# Execution
if __name__ == '__main__':
    populate()
    print_data()
