# Good Reference:
# https://docs.djangoproject.com/en/1.7/ref/models/fields/
# https://docs.djangoproject.com/en/1.7/ref/validators/#built-in-validators

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class TheSimpleModel(models.Model):
    string_field = models.CharField(max_length=20, unique=True)
    integer_field = models.IntegerField(null=True)
    dateTime_field = models.DateTimeField(null=True)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.string_field.ljust(20), self.integer_field, self.dateTime_field)


class TheSimpleChild(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return "Child: {0}".format(self.name)


class TheSimpleParent(models.Model):
    name = models.CharField(max_length=10, unique=True)

    # This can be a model, model name or name of model with namespace
    child = models.ForeignKey(TheSimpleChild)

    def __str__(self):
        return "Parent: {0}".format(self.name, self)


# These models are not applied to the db as they don't inherit from models.Model
class StringFieldTypesExampleModel:
    # CharField and TextField. TextField is for larger quantities of text
    string_field = models.CharField(max_length=10, unique=True)
    text_field = models.TextField()
    email_field = models.EmailField()


class SpecialStringFieldTypesExampleModel:
    # CharField which allows restriction to certain paths!
    field_file_field = models.FilePathField(path="/home/", match="*.txt", recursive=True)
    ip_field = models.GenericIPAddressField(protocol="IPv4")
    slug_field = models.SlugField(max_length=50)  # [a-ZA-Z0-9-_]{0,max_length}
    url_field = models.URLField()


class BooleanFieldTypesExampleModel:
    # BooleanFeld and NullBooleanField
    boolean_field = models.BooleanField()
    null_boolean_field = models.NullBooleanField()


class IntegerFieldTypesExampleModel:
    # Integers
    id_field = models.AutoField(primary_key=True)  # Automatically added if not specified
    bit_int_field = models.BigIntegerField()
    int_field = models.IntegerField()
    pos_int_field = models.PositiveIntegerField()
    small_int_field = models.SmallIntegerField()
    pos_small_int_field = models.PositiveSmallIntegerField
    csv_ints_field = models.CommaSeparatedIntegerField()


class BinaryFieldTypesExampleModel:
    # Binary
    binary_field = models.BinaryField()


class NumberFieldTypesExampleModel:
    # Floating Point Fields
    decimal_field = models.DecimalField()
    float_field = models.FloatField()


class DateFieldTypesExampleModel:
    # Dates
    date_field = models.DateField()
    time_field = models.TimeField()
    date_time_field = models.DateTimeField()


class FilesFieldTypesExampleModel:
    # Files
    file_field = models.FileField(null=True)  # TODO: Dedicate upload example
    image_field = models.ImageField(
        null=True)  # Inherits FieldField though. Validates file is an image and also has height/width property


class FieldOptionsExampleModel:
    OPTION_ONE = 'ONE',
    OPTION_TWO = 'TWO'
    OPTION_ONE_DESC = "This is option 1"
    OPTION_TWO_DESC = "This is option 2"

    OPTIONS = (
        (OPTION_ONE, OPTION_ONE_DESC),
        (OPTION_TWO, OPTION_TWO_DESC)
    )

    name_field = models.CharField(
        null=False,  # If the db is nullable
        blank=True,  # If the form allows empty
        choices=OPTIONS,  # Enum: validates value is contained
        db_column="my_name_field",  # override the database field name created/used
        db_index=True,  # An index to this field will be used
        default=OPTION_ONE,  # The default option
        editable=True,  # If false is not shown in forms for creation/edit
        error_messages={  # Override error messages
                          'required': 'This is required',
                          'invalid': 'This is not a valid value',
                          'invalid_choice': "This is not a valid choice",
                          'unique': 'This is not unique'},
        help_text="This is some help",  # Shown on form and generated documentation
        primary_key=True,  # Makes the field the PK in the db
        unique=True,  # Ensures is unique via validation and db schema
        unique_for_date=True,  # Ensures the date is unique via validation and db schema
        unique_for_month=True,  # Ensure the date month is unique via validation and db schema
        unique_for_year=True,  # Ensures the date year is unique via validation and db schema
        verbose_name="The Fields Name"  # Defaults to the field name, underscores removed and capitalised.
        # Validators - see validators sections TODO: Validators
    )

def is_future_date_validator(value):
    if value <= timezone.now():
        raise ValidationError("{0} is not a future date.".format(value))

class FieldValidatorsExample():
    validated_field = models.CharField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(100),
            RegexValidator("^[A-Z]{1,2}$"),
            is_future_date_validator])


