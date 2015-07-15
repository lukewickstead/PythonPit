import uuid

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, MinLengthValidator, \
    MaxLengthValidator
from django.utils import timezone


# Reference
# https://docs.djangoproject.com/en/1.8/ref/models/
# https://docs.djangoproject.com/en/1.8/ref/models/fields
# https://docs.djangoproject.com/en/1.8/ref/models/options/


class StringFieldTypesExampleModel(models.Model):
    # max_length =  maximum number of characters allowed

    string_field = models.CharField(max_length=10)  # Displays as a text box
    text_field = models.TextField(max_length=100)  # Displays as a text input area instead
    email_field = models.EmailField(max_length=100)  # Provides regex validation for a email address
    csv_ints_field = models.CommaSeparatedIntegerField(max_length=100)  # List of csv integers


class SpecialStringFieldTypesExampleModel(models.Model):
    slug_field = models.SlugField(max_length=50)  # [a-ZA-Z0-9-_]{0,max_length}
    url_field = models.URLField()  # Provides regex validation for URL


class BooleanFieldTypesExampleModel(models.Model):
    boolean_field = models.BooleanField()  # true/false
    null_boolean_field = models.NullBooleanField()  # null/true/false


class IntegerFieldTypesExampleModel(models.Model):
    # Integers
    id_field = models.AutoField(primary_key=True)  # Automatically added if not specified. IntegerField
    bit_int_field = models.BigIntegerField()  # 64 bit; -9223372036854775808 to 9223372036854775807
    int_field = models.IntegerField()  # 32 bit: -2147483648 to 2147483647
    pos_int_field = models.PositiveIntegerField()  # 0 to 2147483647
    small_int_field = models.SmallIntegerField()  # -32768 to 32767
    pos_small_int_field = models.PositiveSmallIntegerField  # 0 to 3276


class BinaryFieldTypesExampleModel(models.Model):
    # Binary
    binary_field = models.BinaryField()


class NumberFieldTypesExampleModel(models.Model):
    # Floating Point Fields

    # max_digits = total number of digits
    # decimal_places = total number of digits after the decimal point

    decimal_field = models.DecimalField(max_digits=8, decimal_places=2)  # Python Decimal type.
    float_field = models.FloatField()  # Python Float type.


class DateFieldTypesExampleModel(models.Model):
    # Dates

    # auto_now: Updates to now upon every save
    # auto_now_add: Updates to now upon record creation

    date_field = models.DateField()
    time_field = models.TimeField()
    date_time_field = models.DateTimeField()

    duration = models.DurationField()  # modeled by Python time delta


class SpecialFieldTypesExampleModel(models.Model):
    models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # A UUID

    ip_field = models.GenericIPAddressField(protocol="IPv4")  # An IP address

    field_file_field = models.FilePathField(path="/home/", match="*.txt", recursive=True)  # A file path


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
