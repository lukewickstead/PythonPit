from django import forms
from django.forms.extras.widgets import SelectDateWidget

from ..models import TITLE_CHOICES, ChildOfOne, ChildManyToMany, ChildOfMany, ModelFieldsToFormFields



# Reference:
# https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/#field-types
# https://docs.djangoproject.com/en/1.8/ref/forms/widgets

YEARS_ = years = (2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009)


class ComplexFormWithWidgets(forms.ModelForm):
    ChoiceField = forms.CharField(max_length=3, widget=forms.Select(choices=TITLE_CHOICES))
    CharField = forms.CharField(max_length=10)
    CommaSeparatedIntegerField = forms.CharField()
    EmailField = forms.EmailField()
    TextField = forms.CharField(widget=forms.Textarea)
    URLField = forms.URLField()

    DateField = forms.DateField()
    DateTimeField = forms.DateTimeField()
    TimeField = forms.TimeField()

    # FileField = models.FileField()
    # ImageField = models.ImageField()
    # FilePathField = forms.FilePathField((match="*.py", recursive=True)

    BigIntegerField = forms.IntegerField(min_value=-9223372036854775808, max_value=9223372036854775807.)
    BooleanField = forms.BooleanField()
    NullBooleanField = forms.NullBooleanField()

    PositiveIntegerField = forms.IntegerField(min_value=0, max_value=2147483647)
    PositiveSmallIntegerField = forms.IntegerField(min_value=0, max_value=32767)
    SlugField = forms.SlugField()
    SmallIntegerField = forms.IntegerField(min_value=-32768, max_value=32767)
    DecimalField = forms.DecimalField()
    FloatField = forms.FloatField()
    IntegerField = forms.IntegerField()
    GenericIPAddressField = forms.GenericIPAddressField()

    # Joins
    ForeignKey = forms.ModelChoiceField(queryset=ChildOfMany.objects.all())
    ManyToManyField = forms.ModelMultipleChoiceField(queryset=ChildManyToMany.objects.all())
    OneToOneField = forms.ModelChoiceField(queryset=ChildOfOne.objects.all())

    # More Widgets
    PasswordInput = forms.CharField(max_length=10, widget=forms.PasswordInput)
    HiddenInput = forms.CharField(max_length=10, widget=forms.HiddenInput, initial='a')
    RadioSelect = forms.CharField(max_length=10, widget=forms.RadioSelect(choices=TITLE_CHOICES))
    CheckboxSelectMultiple = forms.CharField(max_length=10, widget=forms.CheckboxSelectMultiple(choices=TITLE_CHOICES))
    SelectDateWidget = forms.CharField(max_length=10, widget=SelectDateWidget(years=YEARS_))

    # Attrs can be used to pass in data to the html/css
    # attrs={'class': 'special'}

    class Meta:
        model = ModelFieldsToFormFields
        exclude = ()  # Better to set fields explicitly
