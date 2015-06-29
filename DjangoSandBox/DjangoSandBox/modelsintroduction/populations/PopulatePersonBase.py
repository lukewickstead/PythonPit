from datetime import date

from modelsintroduction.models import Person, OPTION_SEX_FEMALE, OPTION_SEX_MALE


class PopulatePersonBase:
    def __init__(self):

        self.raw_data = {
            ("John", 1.85, date(1963, 1, 12), OPTION_SEX_MALE),
            ("Jim", 1.80, date(1946, 2, 1), OPTION_SEX_MALE),
            ("Luke", 1.78, date(1986, 3, 3), OPTION_SEX_MALE),
            ("Dave", 1.82, date(1996, 4, 5), OPTION_SEX_MALE),
            ("Simon", 1.75, date(1965, 5, 15), OPTION_SEX_MALE),
            ("Lynne", 1.65, date(1975, 6, 25), OPTION_SEX_FEMALE),
            ("Claire", 1.70, date(1979, 7, 27), OPTION_SEX_FEMALE),
            ("Sophie", 1.55, date(1974, 8, 12), OPTION_SEX_FEMALE),
            ("Emma", 1.72, date(1977, 8, 13), OPTION_SEX_FEMALE),
            ("Charlotte", 1.68, date(1975, 9, 17), OPTION_SEX_FEMALE)
        }

    @staticmethod
    def display_people():
        for a_model in Person.objects.all():
            print(a_model)

    @staticmethod
    def person_exists(name):
        return Person.objects.filter(name=name).count() >= 1

    def populate(self):
        for name, height, date_of_birth, sex in self.raw_data:
            self.save_person(name, height, date_of_birth, sex)

    @staticmethod
    def save_person(name, height, date_of_birth, sex):
        raise NotImplemented("Save Person is not implemented")
