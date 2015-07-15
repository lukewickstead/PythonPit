import logging

from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'errorsandlogging/index.html')


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


def with_logger(request):
    logger.debug('This is some debug')
    logger.info('This is information')
    logger.warning('This is a warning')
    logger.error('This is a error')
    logger.critical('This is a critical')

    logger.critical("Output with trace", exc_info=True)

    try:
        boom = 1 / 0
        logger.debug("Looks like we have broke the compiler as 1/0 = {0}".format(boom))
    except ZeroDivisionError as e:
        logger.exception(e)

    logger.critical('Final output to show we are logging still')

    return HttpResponse("Logged output")
