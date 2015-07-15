from django.forms import Form, CharField, EmailField, PasswordInput, ValidationError


class UserForm(Form):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    login = CharField()
    email = EmailField()
    password = CharField(widget=PasswordInput)
    password_confirm = CharField(widget=PasswordInput)

    def clean(self):
        super(UserForm, self).clean()

        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Passwords do not match")

        return self.cleaned_data


class UserLoginForm(Form):
    login = CharField()
    password = CharField(widget=PasswordInput)
