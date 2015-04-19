from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from django.utils import timezone

from .models import HelloWorld

def index(request):
    """
    The hello world example.
    :param request: A request object
    :return: A HttpResponse for Hello World!
    """
    return HttpResponse("This would be the hello world example!!!")


def with_template_loader(request):

    template = loader.get_template('helloworld/template_example.html')

    context = RequestContext(request, {'who': "Obelix", 'when': timezone.now(), 'islong' : True} )

    return HttpResponse(template.render(context))


def with_template(request):
    """
    Hello world engaged with a template
    :param request: A request object
    :return: A HttpResponse returned via render; this is a short cut to loader/RequestContext
    """
    context = {'who': "Obelix", 'when': timezone.now(), 'islong' : False}
    return render(request, 'helloworld/template_example.html', context)


def with_model(request):

    hello_model = HelloWorld(first_name="Obelix", now=timezone.now())
    return render(request, 'helloworld/template_with_model_example.html', {'model': hello_model})