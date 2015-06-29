from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSandBox.settings')

import django

django.setup()

from modelsintroduction.populations.PopulatePersonBase import PopulatePersonBase
from modelsintroduction.models import Person


class PopulatePersonByGetOrCreate(PopulatePersonBase):

    @staticmethod
    def save_person(name, height, date_of_birth, sex):
        Person.objects.get_or_create(name=name, sex=sex, height=height, date_of_birth=date_of_birth)


if __name__ == '__main__':
    a_populator = PopulatePersonByGetOrCreate()
    a_populator.populate()
    a_populator.display_people()