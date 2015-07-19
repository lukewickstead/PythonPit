# Reference:
# https://docs.djangoproject.com/en/1.8/topics/http/urls

from django.conf.urls import patterns, include, url
from django.contrib import admin

from home import urls as home_urls
from authmodel import urls as authmodel_urls
from helloworld import urls as helloworld_urls
from ajaxintroduction import urls as ajax_urls
from errorsandlogging import urls as errorsandlogging_urls
from viewsintroduction import urls as viewsintroduction_urls
from formsintroduction import urls as formsintroduction_urls
from sessionsandcookies import urls as sessionsandcookies_urls
from templatesintroduction import urls as templatesintroduction_urls

urlpatterns = \
    patterns('',
             url(r'^$', include(home_urls, namespace="home")),
             url(r'^admin/', include(admin.site.urls)),
             url(r'^home/', include(home_urls, namespace="home")),
             url(r'^auth/', include(authmodel_urls, namespace="auth")),
             url(r'^ajax/', include(ajax_urls, namespace="ajax")),
             url(r'^helloworld/', include(helloworld_urls, namespace="helloworld")),
             url(r'^errorsandlogging/', include(errorsandlogging_urls, namespace="errorsandlogging")),
             url(r'^viewsintroduction/', include(viewsintroduction_urls, namespace="viewsintroduction")),
             url(r'^formsintroduction/', include(formsintroduction_urls, namespace="formsintroduction")),
             url(r'^sessionsandcookies/', include(sessionsandcookies_urls, namespace="sessionsandcookies")),
             url(r'^templatesintroduction/', include(templatesintroduction_urls, namespace="templatesintroduction")),
             )
