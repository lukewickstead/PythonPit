# Good Reference:
# https://docs.djangoproject.com/en/1.8/topics/db/models/
# https://docs.djangoproject.com/en/1.8/ref/models/fields/
# https://docs.djangoproject.com/en/1.8/ref/validators/#built-in-validators

from django.db import models

OPTION_SEX_MALE = 'M'
OPTION_SEX_FEMALE = 'F'
OPTION_SEX_MALE_DESCRIPTION = 'MALE'
OPTION_SEX_FEMALE_DESCRIPTION = 'FEMALE'

OPTIONS_SEX = (
    (OPTION_SEX_MALE, OPTION_SEX_MALE_DESCRIPTION),
    (OPTION_SEX_FEMALE, OPTION_SEX_FEMALE_DESCRIPTION)
)


class Person(models.Model):
    name = models.CharField(max_length=20, unique=True)
    height = models.FloatField()
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1, choices=OPTIONS_SEX)  # get_sex_display() to get the display of MALE/FEMALE
    validated = models.BooleanField(default=False)

    def __str__(self):
        return "{0} - {1} - {2}- {3}- {4}".format(self.name, self.sex, self.date_of_birth, self.height, self.validated)
