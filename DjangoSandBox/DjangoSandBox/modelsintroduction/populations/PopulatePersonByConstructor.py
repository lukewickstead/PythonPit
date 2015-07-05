from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSandBox.settings')

import django

django.setup()

from ..populations.PopulatePersonBase import PopulatePersonBase
from ..models import Person


class PopulatePersonByConstructor(PopulatePersonBase):
    def save_person(self, name, height, date_of_birth, sex):
        if self.person_exists(name):
            return

        a_person = Person(name=name, sex=sex, height=height, date_of_birth=date_of_birth)
        a_person.save()


if __name__ == '__main__':
    a_populator = PopulatePersonByConstructor()
    a_populator.populate()
    a_populator.display_people()
