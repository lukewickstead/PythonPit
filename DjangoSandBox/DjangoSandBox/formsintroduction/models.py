from django.db import models
from django.db.models import Model

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)


class ChildOfMany(Model):
    CharField = models.CharField(max_length=10)

    def __str__(self):
        return self.CharField


class ChildOfOne(Model):
    CharField = models.CharField(max_length=10)

    def __str__(self):
        return self.CharField


class ChildManyToMany(Model):
    CharField = models.CharField(max_length=10)

    def __str__(self):
        return self.CharField

    class Meta:
        verbose_name_plural = "children"


class ModelFieldsToFormFields(Model):
    ChoiceField = models.CharField(max_length=3, choices=TITLE_CHOICES)
    CharField = models.CharField(max_length=10)
    CommaSeparatedIntegerField = models.CharField(max_length=50)
    EmailField = models.EmailField()
    TextField = models.TextField()
    URLField = models.URLField()

    DateField = models.DateField()
    DateTimeField = models.DateTimeField()
    TimeField = models.TimeField()

    # FileField = models.FileField()
    # ImageField = models.ImageField()
    # FilePathField = models.FilePathField()

    BigIntegerField = models.BigIntegerField()
    BooleanField = models.BooleanField()
    NullBooleanField = models.NullBooleanField()

    PositiveIntegerField = models.PositiveIntegerField()
    PositiveSmallIntegerField = models.PositiveSmallIntegerField()
    SlugField = models.SlugField()
    SmallIntegerField = models.SmallIntegerField()
    DecimalField = models.DecimalField(decimal_places=2, max_digits=5)
    FloatField = models.FloatField()
    IntegerField = models.IntegerField()
    GenericIPAddressField = models.GenericIPAddressField()

    # Joins
    ForeignKey = models.ForeignKey(ChildOfMany)
    ManyToManyField = models.ManyToManyField(ChildManyToMany)
    OneToOneField = models.OneToOneField(ChildOfOne)
