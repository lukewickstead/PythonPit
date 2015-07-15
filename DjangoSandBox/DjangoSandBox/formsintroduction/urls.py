from django.conf.urls import patterns, url

from . import views

urlpatterns = \
    patterns('',
             url(r'^$', views.index, name="index"),
             url(r'^basic/$', views.basic, name="form_basic"),
             url(r'^basichtml/$', views.basic_html, name="form_basic_html"),
             url(r'^class/create/$', views.class_form, name="form_class_create"),
             url(r'^class/(?P<pk>[0-9]+)/edit/$', views.class_form, name="form_class_edit"),
             url(r'^factory/create/$', views.model_form_factory_form, name="form_factory_create"),
             url(r'^factory/(?P<pk>[0-9]+)/edit/$', views.model_form_factory_form, name="form_factory_edit"),
             url(r'^complete_model/create/$', views.complete_model_example, name="form_complete_create"),
             url(r'^complete_model/(?P<pk>[0-9]+)/edit/$', views.complete_model_example, name="form_complete_edit")
             )
