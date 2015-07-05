from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSandBox.settings')

import django

django.setup()

from modelsintroduction.populations.PopulatePersonBase import PopulatePersonBase
from modelsintroduction.models import Person


class PopulatePersonByCreate(PopulatePersonBase):
    def save_person(self, name, height, date_of_birth, sex):
        if self.person_exists(name):
            return

        Person.objects.create(name=name, sex=sex, height=height, date_of_birth=date_of_birth)


if __name__ == '__main__':
    a_populator = PopulatePersonByCreate()
    a_populator.populate()
    a_populator.display_people()
