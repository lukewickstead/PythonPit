from django.conf.urls import patterns, url

from . import views

urlpatterns = \
    patterns('',
             url(r'^$', views.index, name="index"),

             url(r'^sessions/$', views.sessions, name="sessions"),
             url(r'^sessions/clear/$', views.sessions_clear, name="sessions_clear"),

             url(r'^cookies/$', views.cookies, name="cookies"),
             url(r'^cookies/test$', views.cookies_test, name="cookies_test"),
             url(r'^cookies/expire', views.cookies_expire, name="cookies_expire"),
             )
