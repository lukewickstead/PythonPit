from django import forms
from ..validators import validate_name

# Reference:
# https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/#field-types

error_name = {
    'required': 'You must enter a name!',
    'invalid': 'Invalid name format.'
}


class BasicFormExample(forms.Form):
    name = forms.CharField(label="Name", min_length=3, max_length=30, error_messages=error_name,
                           initial="Jim", validators=[validate_name])

    height = forms.DecimalField(max_value=2, help_text="Height in meters", label="Height (M.CM)", decimal_places=2)

    def clean(self):
        cleaned_data = super(BasicFormExample, self).clean()

        name = cleaned_data.get("name")
        height = cleaned_data.get("height")

        if name is None and height is None:
            msg = "Both name and height are required!!!"
            self.add_error('name', msg)
            self.add_error('height', msg)
            raise forms.ValidationError(msg)

        return self.cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if " " in name:
            raise forms.ValidationError("No spaces in the name please")

        return name
