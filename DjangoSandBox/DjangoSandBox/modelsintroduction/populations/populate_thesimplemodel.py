from os import environ
from datetime import timedelta

from django.utils import timezone

environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSandBox.settings')

import django

django.setup()

from modelsintroduction.models import TheSimpleModel

data_elements = {
    ("Hello", 1, timezone.now()),
    ("Bob", 2, timezone.now() - timedelta(days=1)),
    ("Smithy", 3, timezone.now() - timedelta(days=1)),
    ("Bye", 4, timezone.now() - timedelta(days=1))
}


def populate():
    for the_string, the_int, the_datetime in data_elements:
        save_model(the_string, the_int, the_datetime)

    for a_model in TheSimpleModel.objects.all():
        print(a_model)


def save_model(the_string, the_int, the_datetime):
    the_model_instance = get_model(the_string)
    the_model_instance.integer_field = the_int
    the_model_instance.dateTime_field = the_datetime
    the_model_instance.save()


def get_model(the_string):
    return TheSimpleModel.objects.get_or_create(string_field=the_string)[0]

# Execution
if __name__ == '__main__':
    print("Populating TheSimpleModel")
    populate()