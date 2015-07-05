from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSandBox.settings')

import django

django.setup()

from modelsintroduction.populations.PopulatePersonBase import PopulatePersonBase
from modelsintroduction.models import Person


class PopulatePersonByBulkCreate(PopulatePersonBase):
    def __init__(self):
        super().__init__()
        self.people = []

    def save_person(self, name, height, date_of_birth, sex):
        if self.person_exists(name):
            return

        self.people.append(Person(name=name, sex=sex, height=height, date_of_birth=date_of_birth))

    def populate(self):
        super().populate()
        Person.objects.bulk_create(self.people)


if __name__ == '__main__':
    a_populator = PopulatePersonByBulkCreate()
    a_populator.populate()
    a_populator.display_people()
