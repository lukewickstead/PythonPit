from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseNotAllowed
from django.shortcuts import render, redirect, render_to_response
from django.template import loader, RequestContext
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_GET, require_POST

# Reference:
# https://docs.djangoproject.com/en/1.8/ref/views/
# https://docs.djangoproject.com/en/1.8/ref/request-response

# https://docs.djangoproject.com/en/1.8/topics/http/views
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


def sessions(request):
    """
    django.contrib.sessions.models.Session need to be enabled in the installed_apps of the settings.py
    """

    context = {
        "has_visited": request.session.get("has_visited", False),
        "visited": request.session.get("visited", None),
        "expiry": request.session.get_expiry_date().strftime("%x %X")
    }

    if "has_visited" not in request.session:
        request.session['has_visited'] = str(True)
        request.session['visited'] = datetime.now().strftime("%x %X")
        request.session.set_expiry(10)  # Time in seconds. 0 expires when the browser is closed

    return render(request, 'helloworld/sessions.html', context)


def sessions_clear(request):
    if 'has_visited' in request.session:
        del request.session['has_visited']

    request.session.clear()

    return redirect(reverse("helloworld:sessions"))


def cookies_test(request):
    can_create_cookie = False
    request.session.set_test_cookie()

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        can_create_cookie = True

    return render(request, "helloworld/cookies_test.html", {"can_create_cookie": can_create_cookie})


def cookies(request):
    hits = int(request.COOKIES.get('hits', '0'))

    # hits = int(request.COOKIES.get('hits', '0'))
    # print(request.COOKIES['HTTP_COOKIE'].get_expiry_age())

    first_hit = 'hits' not in request.COOKIES

    response = render_to_response('helloworld/cookies.html',
                                  {"first_hit": first_hit, "hits": hits},
                                  RequestContext(request))

    response.set_cookie('hits', hits + 1, max_age=30)
    return response


def cookies_expire(request):
    response = render_to_response('helloworld/cookies_clear.html',
                                  {"first_hit": True, "hits": 0},
                                  RequestContext(request))

    response.delete_cookie('hits')
    return response


@require_http_methods(["GET", "POST"])
def error_if_not_get_or_post(request):
    return HttpResponse("This can only be called with a get or a post")


@require_POST
def error_if_not_post(request):
    return HttpResponse("{0}, this can only be called with a post".format(request.POST.get("name", "")))


@require_GET
def error_if_not_get(request):
    return HttpResponse("This can only be called with a get")


def error_as_custom_404(request):
    return HttpResponseNotFound('<h1>There is nothing to see here</h1>')


def error_as_404(request):
    raise Http404("There is nothing to see here")


def not_allowed(request):
    return HttpResponseNotAllowed("<h1>You are not allowed to see this</h1>")
