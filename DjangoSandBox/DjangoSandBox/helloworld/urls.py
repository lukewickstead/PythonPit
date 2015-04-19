from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^index$', views.index, name="index"),
    url(r'^template$', views.with_template, name="template"),
    url(r'^model$', views.with_model, name="model"),
    url(r'^template_loader$', views.with_template_loader, name="loader"),
)