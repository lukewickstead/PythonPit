from re import match
from django.core.exceptions import ValidationError


def validate_name(a_string):
    a_match = match(r"[A-Z][a-z]{2,}$", a_string)
    if a_match:
        return True

    raise ValidationError("Name must be a capitalised single word")
