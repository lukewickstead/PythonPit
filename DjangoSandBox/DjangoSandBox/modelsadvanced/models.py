from datetime import date

from django.db import models
from django.db.models import Model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, MinLengthValidator, \
    MaxLengthValidator


#
# Examples of joins, inheritance and validation
#

# **** MISC Notes ****
#
# When saving a model, if PK is "" or null the generated sql creates an insert otherwise creates an update
#
# Save() can be passed a collection of fields to save; non referenced fields are not saved even if they
# have been modified.
#   a_person.save(update_fields=["name", "sex"])
#
# Models can have their data re-retrieved from the db with the refresh_from_db function
#   Model.refresh_from_db(using=None, fields=None, **kwargs)
#
# Model equality (__eq__ ) is based upon the equality of the PK and class type. If the class type is a proxy then this
# equates to the first non proxy class in the ancestry.


# **** JOINS ****
#
# OneToOneField: A 1:1 relationship
# ForeignKey: A 1:n relationship.
# ManyToManyField: A n:m relationship

# If accessing joined record where the end is a single entity (1:1, 1:n), the join is optional and also no associated
# record has been saved, a ObjectDoesNotExist error is raised.

# OneToOneField: A 1:1 relationship
class Man(Model):
    """ An example of 1:1 join between a man and his dog """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Dog(Model):
    """ An example of 1:1 join between a man and his dog """
    name = models.CharField(max_length=20)
    owner = models.OneToOneField(Man, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


# ForeignKey: A 1:n relationship.
class Parent(Model):
    """ An example of a 1:n join between a parent and their children """
    name = models.CharField(max_length=10, unique=True, null=True)

    def __str__(self):
        return self.name


class Child(Model):
    """ An example of a 1:n join between a parent and their children """
    name = models.CharField(max_length=10, unique=True)
    parent = models.ForeignKey(Parent, null=True)

    # models.ForeignKey(Parent, related_name=children)
    # The above would rename child_set to children when traversing the join from the parent record

    def __str__(self):
        return self.name


# ManyToManyField: A n:m relationship
class Author(Model):
    """ An example of a n:m join between Authors and Books """
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Book(Model):
    """ An example of a n:m join between Authors and Books """
    authors = models.ManyToManyField(Author)
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


# *** MODEL EXTENDING / INHERITANCE ***

# 01: Duplicate Fields
# 02: Abstract Parent
# 03: Multi-Parent base Child
# 04: Proxy

# 02: Abstract Parent
class AbstractBaseParent(Model):
    """ An example of abstract model inheritance """
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class AbstractBaseChild(AbstractBaseParent):
    """ An example of abstract model inheritance """
    age = models.IntegerField()

    def __str__(self):
        return "Name: {0}, Age: {1}".format(self.name, self.age)


# 03: Multi-Parent base Child
class MultiTableBaseParent(Model):
    """ An example of abstract model inheritance """
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


# 04: Proxy
class MultiTableBaseChild(MultiTableBaseParent):
    """ An example of abstract model inheritance """
    age = models.IntegerField()

    def __str__(self):
        return "Name: {0}, Age: {1}".format(self.name, self.age)


# 04: Proxy
class ProxyParent(Model):
    """ An example of proxy model inheritance """
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class ProxyChild(ProxyParent):
    """
    An example of proxy model inheritance.
    A proxy saves and reads from the original table though you can independently set class Meta or the default object
    manager without affecting the original table
    """

    class Meta:
        proxy = True


# *** Model Validation ***
#
# When using forms you call is_valid() though to ensure all validation is called otherwise you call full_clean().
#
# The functions is_valid() and full_clean() calls the following functions
#
# 01: Model.clean_fields() which validates the model's fields
# 02: Model.clean() which validates the model as a whole entity
# 03: Model.validate_unique() which validate the field uniqueness against the db and any field constraints.
#
# Simply calling save() upon a model does not raise validation; only database schema constraints will be raised.
#
# All functions allow include/exclude fields to control which fields are validated against.

def is_future_date_validator(value):
    if value <= date.today():
        raise ValidationError("{0} is not a future date.".format(value))


class ContactDetails(Model):
    def clean(self):
        """
        A hook for custom validation, probably where db access is required to cross field validation
        """

        if self.name == 'Luke':
            raise ValidationError({'name': "Luke is barred"}, code="Invalid")

    age = models.IntegerField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(100)])

    name = models.CharField(max_length=20,
                            validators=[
                                MinLengthValidator(10),
                                MaxLengthValidator(10),
                                RegexValidator("^[A-Z][a-z]{1,}$")])

    contactDate = models.DateField(
        validators=[
            is_future_date_validator])

# Model Meta Options can be used for various configs from ordering, table names etc.
# Reference:
# https://docs.djangoproject.com/en/1.8/ref/models/options/

# Managers can be used provident different perspectives of the data.
#
# Reference:
# https://docs.djangoproject.com/en/1.8/topics/db/managers/
