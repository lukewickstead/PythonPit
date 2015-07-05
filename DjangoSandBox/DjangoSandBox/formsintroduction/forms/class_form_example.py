from django import forms
from django.forms import ModelForm

from viewsintroduction.models import PhoneAddress
from ..validators import validate_name


class ClassBasedForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClassBasedForm, self).__init__(*args, **kwargs)
        self.fields["city"].validators.append(validate_name)

    def clean(self):
        cleaned_data = super(ClassBasedForm, self).clean()

        city = cleaned_data.get("city")
        street_name = cleaned_data.get("street_name")
        number = cleaned_data.get("number")

        if city is None and street_name is None and number is None:
            msg = "None of the fields have been set!!!"
            for a_field in ('city', 'street_name', 'number'):
                self.add_error(a_field, msg)
            raise forms.ValidationError(msg)

        return self.cleaned_data

    def clean_city(self):
        city = self.cleaned_data.get("city")

        if " " in city:
            raise forms.ValidationError("No spaces in the city name please")

        return city

    class Meta:
        model = PhoneAddress
        fields = ("city", "street_name", "number")
        labels = {'number': "House No."}
        help_texts = {'number': "This is the number of the house."}
        error_messages = {
            'number': {
                'required': "We need a number of the house!",
                'max_length': "We only accept houses up to 20!"}
        }
