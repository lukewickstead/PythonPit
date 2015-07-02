from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseNotAllowed
from django.shortcuts import render
from django.template import loader, RequestContext
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_GET, require_POST

# Reference:
# https://docs.djangoproject.com/en/1.8/topics/http/views
# https://docs.djangoproject.com/en/1.8/ref/request-response
# https://docs.djangoproject.com/en/1.8/topics/http/shortcuts
# https://docs.djangoproject.com/en/1.8/topics/http/decorators
# https://docs.djangoproject.com/en/1.8/topics/http/views/#returning-errors
# https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/#redirect
# https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/#get-object-or-404
# https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/#get-list-or-404
# https://docs.djangoproject.com/en/1.8/ref/views/

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


@require_http_methods(["GET", "POST"])
def error_if_not_get_or_post(request):
    return HttpResponse("This can only be called with a get or a post")


@require_POST
def error_if_not_post(request):
    return HttpResponse("This can only be called with a post")


@require_GET
def error_if_not_get(request):
    return HttpResponse("This can only be called with a get")


def error_as_custom_404(request):
    return HttpResponseNotFound('<h1>There is nothing to see here</h1>')


def error_as_404(request):
    raise Http404("There is nothing to see here")


def not_allowed(request):
    return HttpResponseNotAllowed("<h1>You are not allowed to see this</h1>")
