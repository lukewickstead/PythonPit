from django.db import models
from django.db.models import Model
from django.core.urlresolvers import reverse

OPTION_SEX_MALE = 'M'
OPTION_SEX_FEMALE = 'F'
OPTION_SEX_MALE_DESCRIPTION = 'MALE'
OPTION_SEX_FEMALE_DESCRIPTION = 'FEMALE'

OPTIONS_SEX = (
    (OPTION_SEX_MALE, OPTION_SEX_MALE_DESCRIPTION),
    (OPTION_SEX_FEMALE, OPTION_SEX_FEMALE_DESCRIPTION)
)


class PhoneAddress(Model):
    number = models.IntegerField()
    street_name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return "{0} {1} {2}".format(self.number, self.street_name, self.city)

    def get_absolute_url(self):
        return reverse('viewsintroduction:address', args=[self.id])


class PhoneContact(Model):
    name = models.CharField(max_length=20, unique=True)
    surname = models.CharField(max_length=20, unique=True)

    height = models.FloatField()
    date_of_birth = models.DateField()
    is_family = models.BooleanField(default=False)
    sex = models.CharField(max_length=1, choices=OPTIONS_SEX)

    address = models.OneToOneField(PhoneAddress)

    def __str__(self):
        return "{0} {1}".format(self.name, self.surname)

    def get_absolute_url(self):
        return reverse('viewsintroduction:contact', args=[self.id])
