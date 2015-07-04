from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = \
    patterns('',
             url(r'^$', views.index, name="index"),
             url(r'^users/$', views.users, name="users"),
             url(r'^users2/$', login_required(views.users), name="users2"),
             url(r'^login/$', views.login_page, name="login"),
             url(r'^logout/$', views.logout_page, name="logout"),
             url(r'^login/create/$', views.create_login, name="login_create")
             )
