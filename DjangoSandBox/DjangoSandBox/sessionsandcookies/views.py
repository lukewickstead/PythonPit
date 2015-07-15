from datetime import datetime
import logging

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'sessionsandcookies/index.html')


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

    return render(request, 'sessionsandcookies/sessions.html', context)


def sessions_clear(request):
    if 'has_visited' in request.session:
        del request.session['has_visited']

    request.session.clear()

    return redirect(reverse("sessionsandcookies:sessions"))


def cookies_test(request):
    can_create_cookie = False
    request.session.set_test_cookie()

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        can_create_cookie = True

    return render(request, "sessionsandcookies/cookies_test.html", {"can_create_cookie": can_create_cookie})


def cookies(request):
    hits = int(request.COOKIES.get('hits', '0'))

    # hits = int(request.COOKIES.get('hits', '0'))
    # print(request.COOKIES['HTTP_COOKIE'].get_expiry_age())

    first_hit = 'hits' not in request.COOKIES

    response = render_to_response('sessionsandcookies/cookies.html',
                                  {"first_hit": first_hit, "hits": hits},
                                  RequestContext(request))

    response.set_cookie('hits', hits + 1, max_age=30)
    return response


def cookies_expire(request):
    response = render_to_response('sessionsandcookies/cookies_clear.html',
                                  {"first_hit": True, "hits": 0},
                                  RequestContext(request))

    response.delete_cookie('hits')
    return response
