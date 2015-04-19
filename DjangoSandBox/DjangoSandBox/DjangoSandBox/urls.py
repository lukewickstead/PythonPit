from django.conf.urls import patterns, include, url
from django.contrib import admin

from helloworld import urls as helloworld_urls
from modelsintroduction import urls as modelsintroduction_urls
from templatesintroduction import urls as templatesintroduction_urls

urlpatterns = patterns('',
    url(r'^$', include(helloworld_urls, namespace="helloworld")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^helloworld/', include(helloworld_urls, namespace="helloworld")),
    url(r'^templatesintroduction/', include(templatesintroduction_urls, namespace="templatesintroduction")),

)
