from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

# Good References:
# https://docs.djangoproject.com/en/1.7/ref/templates/builtins


def dates(request):
    context = {
        'when': timezone.now(),
        'yesterday': timezone.now() - timedelta(days=1),
        'tomorrow': timezone.now() + timedelta(days=1)
    }

    return render(request, 'templatesintroduction/dates_and_times.html', context)


def strings(request):
    context = {
        'who': "Asterix et Obelix",
        'False': False,
        'True': True,
        'None': None,
        'colours': {'Red', 'Blue', 'Green'},
        'longmessage': 'This is a really really really long message.',
        'longboldmessage': '<p><b>This is a really really really long message which is in bold</b>.</p>',
        'messagewithnewlines': "This\ncontains\nnewlines"
    }

    return render(request, 'templatesintroduction/strings.html', context)


def collections(request):
    context = {'colours': {'Red', 'Blue', 'Green'},
               'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
               'duplicatednumbers': [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3],
               'worldcities': {'UK': ['Plymouth', 'Bristol'], 'France': ['Grenoble']},
               'lettersandordinals': [(1, 'a'), (2, 'b'), (3, 'c')],
               'emptycollection': [],
               'boysandgirls': [
                   {'name': 'Lukelad', 'age': 26, 'sex': 'male'},
                   {'name': 'Lukette', 'age': 66, 'sex': 'female'},
                   {'name': 'Luke', 'age': 36, 'sex': 'male'},
                   {'name': 'Lukecy', 'age': 36, 'sex': 'female'}]}

    return render(request, 'templatesintroduction/collections.html', context)


def conditions(request):
    context = {
        'age': 20,
        'valueone': 1,
        'valuetwo': 2,
        'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }

    return render(request, 'templatesintroduction/conditions.html', context)


def index(request):
    context = {}
    return render(request, 'templatesintroduction/index.html', context)


def numbers(request):
    context = {
        'onetwo': [1, 2]
    }

    return render(request, 'templatesintroduction/numbers.html', context)


def extension(request):
    return render(request, 'templatesintroduction/template_extension_example.html')


def urls(request):
    return render(request, 'templatesintroduction/urls.html')


def includes(request):
    context = {
        'msg': "This is a message of hello!!!"
    }

    return render(request, 'templatesintroduction/includes.html', context)


def debug(request):
    return render(request, 'templatesintroduction/debug.html')


def static_files(request):
    return render(request, 'templatesintroduction/static_files.html')
