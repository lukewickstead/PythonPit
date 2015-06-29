from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from django.utils import timezone
from django.views.decorators.http import require_http_methods

# Reference:
# https://docs.djangoproject.com/en/1.8/topics/http/views
# https://docs.djangoproject.com/en/1.8/ref/request-response
# https://docs.djangoproject.com/en/1.8/topics/http/shortcuts
# https://docs.djangoproject.com/en/1.8/topics/http/decorators

from .models import HelloWorld


def index(request):
    return render(request, 'helloworld/index.html')


def hello(request):
    """
    The hello world example.
    :param request: A request object
    :return: A HttpResponse for Hello World!
    """
    return HttpResponse("This would be the hello world example!!!")


def with_template_loader(request):
    template = loader.get_template('helloworld/template_example.html')

    context = RequestContext(request, {'who': "Obelix", 'when': timezone.now(), 'islong': True})

    return HttpResponse(template.render(context))


def with_template(request):
    """
    Hello world engaged with a template
    :param request: A request object
    :return: A HttpResponse returned via render; this is a short cut to loader/RequestContext
    """

    # This is a shortcut to the template loader/ RequestContext
    context = {'who': "Obelix", 'when': timezone.now(), 'islong': False}
    return render(request, 'helloworld/template_example.html', context)


def with_model(request):
    hello_model = HelloWorld(first_name="Obelix", now=timezone.now())
    return render(request, 'helloworld/template_with_model_example.html', {'model': hello_model})


# @require_POST()
# @require_GET
@require_http_methods(["GET", "POST"])
def with_decorator(request):
    # This view will return a django.http.HttpResponseNotAllowed  if the request is not a Get/Post
    pass

# TODO: ErrorCodes https://docs.djangoproject.com/en/1.8/topics/http/views/#returning-errors
# TODO: Redirect https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/#redirect
# TODO: https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/#get-object-or-404
# TODO: https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/#get-list-or-404
# https://docs.djangoproject.com/en/1.8/ref/views/