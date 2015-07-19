from django.conf.urls import patterns, url

from . import views

urlpatterns = \
    patterns('',
             url(r'^$', views.get_quotes, name="index"),
             url(r'^random/$', views.get_random_quote, name="random"),
             url(r'^author/$', views.get_author_quotes, name="auth"),
             url(r'^new/$', views.new_quote, name="new"),
             )
