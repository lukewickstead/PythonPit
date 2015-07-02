from django.conf.urls import patterns, include, url
from django.contrib import admin

from helloworld import urls as helloworld_urls
from home import urls as home_urls
from templatesintroduction import urls as templatesintroduction_urls
from viewsintroduction import urls as viewsintroduction_urls
from formsintroduction import urls as formsintroduction_urls

# Reference: https://docs.djangoproject.com/en/1.8/topics/http/urls

urlpatterns = \
    patterns('',
             url(r'^$', include(home_urls, namespace="home")),
             url(r'^admin/', include(admin.site.urls)),
             url(r'^home/', include(home_urls, namespace="home")),
             url(r'^helloworld/', include(helloworld_urls, namespace="helloworld")),
             url(r'^viewsintroduction/', include(viewsintroduction_urls, namespace="viewsintroduction")),
             url(r'^formsintroduction/', include(formsintroduction_urls, namespace="formsintroduction")),
             url(r'^templatesintroduction/', include(templatesintroduction_urls, namespace="templatesintroduction")),
             )
