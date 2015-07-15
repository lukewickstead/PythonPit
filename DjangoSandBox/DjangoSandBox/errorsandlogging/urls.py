from django.conf.urls import patterns, url

from . import views

urlpatterns = \
    patterns('',
             url(r'^$', views.index, name="index"),
             url(r'^errors/post_or_get/$', views.error_if_not_get_or_post, name="error_if_not_get_or_post"),
             url(r'^errors/404/$', views.error_as_404, name="error_as_404"),
             url(r'^errors/custom_404/$', views.error_as_custom_404, name="error_as_custom_404"),
             url(r'^errors/not_allowed/$', views.not_allowed, name="not_allowed"),
             url(r'^errors/only_get/$', views.error_if_not_get, name="error_if_not_get"),
             url(r'^errors/only_post/$', views.error_if_not_post, name="error_if_not_post"),

             url(r'^logger/$', views.with_logger, name="logger")
             )
