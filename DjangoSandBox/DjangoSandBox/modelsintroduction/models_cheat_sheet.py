from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, MinLengthValidator, \
    MaxLengthValidator
from django.utils import timezone


class StringFieldTypesExampleModel(models.Model):
    # CharField and TextField. TextField is for larger quantities of text
    string_field = models.CharField(max_length=10, unique=True)
    text_field = models.TextField()
    email_field = models.EmailField()


class SpecialStringFieldTypesExampleModel(models.Model):
    # CharField which allows restriction to certain paths!
    field_file_field = models.FilePathField(path="/home/", match="*.txt", recursive=True)
    ip_field = models.GenericIPAddressField(protocol="IPv4")
    slug_field = models.SlugField(max_length=50)  # [a-ZA-Z0-9-_]{0,max_length}
    url_field = models.URLField()


class BooleanFieldTypesExampleModel(models.Model):
    # BooleanFeld and NullBooleanField
    boolean_field = models.BooleanField()
    null_boolean_field = models.NullBooleanField()


class IntegerFieldTypesExampleModel(models.Model):
    # Integers
    id_field = models.AutoField(primary_key=True)  # Automatically added if not specified
    bit_int_field = models.BigIntegerField()
    int_field = models.IntegerField()
    pos_int_field = models.PositiveIntegerField()
    small_int_field = models.SmallIntegerField()
    pos_small_int_field = models.PositiveSmallIntegerField
    csv_ints_field = models.CommaSeparatedIntegerField()


class BinaryFieldTypesExampleModel(models.Model):
    # Binary
    binary_field = models.BinaryField()


class NumberFieldTypesExampleModel(models.Model):
    # Floating Point Fields
    decimal_field = models.DecimalField()
    float_field = models.FloatField()


class DateFieldTypesExampleModel(models.Model):
    # Dates
    date_field = models.DateField()
    time_field = models.TimeField()
    date_time_field = models.DateTimeField()


class FilesFieldTypesExampleModel(models.Model):
    # Files
    file_field = models.FileField(null=True)

    # Inherits FieldField though. Validates file is an image and also has height/width property
    image_field = models.ImageField(null=True)


class FieldOptionsExampleModel(models.Model):
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
        verbose_name="The Fields Name",  # Defaults to the field name, underscores removed and capitalised.
        validators=[MinLengthValidator(10)]
    )


def custom_validator(value):
    if value <= timezone.now():
        raise ValidationError("{0} is not a future date.".format(value))


class FieldValidatorsExample(models.Model):
    validated_field = models.CharField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(100),
            MinLengthValidator(10),
            MaxLengthValidator(10),
            RegexValidator("^[A-Z]{1,2}$"),
            custom_validator])


class DbIndexedModelExample(models.Model):
    """
    This model will have two indexes; {one} and {two, three}
    """
    one = models.CharField(db_index=True)
    two = models.CharField()
    three = models.CharField()

    class Meta:
        index_together = ["two", "three"]
