from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSandBox.settings')

import django

django.setup()

from modelsadvanced.models import Man, Dog

men_names = ["Luke", "Dave", "Angus"]
dog_names = ["Fido", "Duke", "Buster"]


def populate():
    for man_name, dog_name in zip(men_names, dog_names):
        a_man = save_man(man_name)
        save_dog(dog_name, a_man)


def print_data():
    print("*Man --> Dog")
    for aMan in Man.objects.all():
        print("{0} --> {1}".format(aMan, aMan.dog))

    print("*Dog --> Man")
    for a_dog in Dog.objects.all():
        print("{0} --> {1}".format(a_dog, a_dog.owner))


def save_dog(name, owner):
    return Dog.objects.get_or_create(name=name, defaults={'owner': owner})[0]


def save_man(name):
    return Man.objects.get_or_create(name=name)[0]

# Execution
if __name__ == '__main__':
    populate()
    print_data()
