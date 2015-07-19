import json
from random import randint

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Quote


# Reference:
# https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
# http://plugins.jquery.com/cookie/

def get_quotes(request):
    authors = set(r.author for r in Quote.objects.all())

    return render(request, "ajaxintroduction/random_quotes.html", context={"authors": authors})


def get_random_quote(request):
    random_number = randint(0, Quote.objects.all().count() - 1)

    random_quote = Quote.objects.all()[random_number]
    context_data = {random_quote.author: random_quote.quote}

    return HttpResponse(json.dumps(context_data), content_type="application/json")


def get_author_quotes(request):
    if "author" not in request.GET or request.GET["author"] == "all":
        quotes = Quote.objects.all()
    else:
        author_name = request.GET["author"]
        quotes = Quote.objects.filter(author=author_name)

    return HttpResponse(serializers.serialize('json', quotes), content_type="application/json", )


# @csrf_exempt
def new_quote(request):
    message = ""

    is_valid = True
    created = False

    print(request.POST)

    if "quote" not in request.POST or "author" not in request.POST:
        message = "Invalid post data"
        is_valid = False

    if request.POST["quote"] == "" or request.POST["author"] == "":
        message = "Please provide a quote and an author"
        is_valid = False

    if is_valid:
        quote, created = Quote.objects.get_or_create(quote=request.POST["quote"], author=request.POST["author"])

        if created:
            message = "Quote Created"
        else:
            message = "Quote already exists"

    data = {"count": Quote.objects.all().count(), "message": message, "created": created}

    return JsonResponse(data)
