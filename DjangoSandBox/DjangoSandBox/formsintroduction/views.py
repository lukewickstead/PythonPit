from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms.bastic_form_example import BasicFormExample
from .forms.class_form_example import ClassBasedForm
from .forms.complex_form_with_widgets import ComplexFormWithWidgets
from .models import ModelFieldsToFormFields
from viewsintroduction.models import PhoneAddress


def index(request):
    return render(request, 'formsintroduction/index.html')


def basic(request):
    if request.POST:
        form = BasicFormExample(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            height = form.cleaned_data['height']

            return HttpResponse("{0} is {1} tall".format(name, height))
        else:
            return render(request, "formsintroduction/basic_form_example.html", {'form': form})
    else:
        form = BasicFormExample()
        return render(request, 'formsintroduction/basic_form_example.html', {'form': form})


def basic_html(request):
    if request.POST:
        form = BasicFormExample(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            height = form.cleaned_data['height']

            return HttpResponse("{0} is {1} tall".format(name, height))
        else:
            return render(request, "formsintroduction/basic_form_with_html_example.html", {'form': form})
    else:
        form = BasicFormExample()
        return render(request, 'formsintroduction/basic_form_with_html_example.html', {'form': form})


def class_form(request, pk=None):
    if pk:
        an_address = get_object_or_404(PhoneAddress, pk=pk)
        form = ClassBasedForm(request.POST or None, instance=an_address)
    else:
        form = ClassBasedForm(request.POST or None, initial={'city': 'Plymouth'})

    if request.POST and form.is_valid():
        an_address = form.save(commit=True)
        return redirect(an_address)
    else:
        return render(request, 'formsintroduction/class_based_form_example.html', {'form': form})


def model_form_factory_form(request, pk=None):
    phone_address_form = modelform_factory(PhoneAddress, fields=("city", "street_name", "number"))

    if pk:
        an_address = get_object_or_404(PhoneAddress, pk=pk)
        form = phone_address_form(request.POST or None, instance=an_address)
    else:
        form = phone_address_form(request.POST or None)

    if request.POST and form.is_valid():
        an_address = form.save(commit=True)
        return redirect(an_address)
    else:
        return render(request, 'formsintroduction/form_factory_example.html', {'form': form})


def complete_model_example(request, pk=None):
    if pk:
        an_instance = get_object_or_404(ModelFieldsToFormFields, pk=pk)
        form = ComplexFormWithWidgets(request.POST or None, instance=an_instance)
    else:
        form = ComplexFormWithWidgets(request.POST or None)

    if request.POST and form.is_valid():
        if form.is_valid():
            an_instance = form.save(commit=True)
            return HttpResponse("Created with id={0}".format(an_instance.id))
    else:
        return render(request, 'formsintroduction/complete_model_form_example.html', {'form': form})
