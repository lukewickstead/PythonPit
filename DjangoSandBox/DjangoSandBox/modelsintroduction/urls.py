from django.conf.urls import patterns, url

from modelsintroduction.views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^index$', IndexView.as_view(), name="index"),
)