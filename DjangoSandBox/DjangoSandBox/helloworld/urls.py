from django.conf.urls import patterns, url

from . import views

urlpatterns = \
    patterns('',
             url(r'^$', views.index, name="default"),
             url(r'^index/$', views.index, name="index"),
             url(r'^hello/$', views.hello, name="hello"),
             url(r'^template/$', views.with_template, name="template"),
             url(r'^model/$', views.with_model, name="model"),
             url(r'^template_loader/$', views.with_template_loader, name="loader"),

             url(r'^sessions/$', views.sessions, name="sessions"),
             url(r'^sessions/clear/$', views.sessions_clear, name="sessions_clear"),

             url(r'^cookies/$', views.cookies, name="cookies"),
             url(r'^cookies/test$', views.cookies_test, name="cookies_test"),
             url(r'^cookies/expire', views.cookies_expire, name="cookies_expire"),

             url(r'^errors/post_or_get/$', views.error_if_not_get_or_post, name="error_if_not_get_or_post"),
             url(r'^errors/404/$', views.error_as_404, name="error_as_404"),
             url(r'^errors/custom_404/$', views.error_as_custom_404, name="error_as_custom_404"),
             url(r'^errors/not_allowed/$', views.not_allowed, name="not_allowed"),
             url(r'^errors/only_get/$', views.error_if_not_get, name="error_if_not_get"),
             url(r'^errors/only_post/$', views.error_if_not_post, name="error_if_not_post")
             )
