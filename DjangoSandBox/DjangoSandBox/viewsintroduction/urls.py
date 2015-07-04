# urls.py
from viewsintroduction.views import PhoneAddressListView, PhoneAddressCreateView, PhoneAddressDeleteView, \
    PhoneAddressDetailView, PhoneAddressUpdateView, PhoneContactCreateView, PhoneContactDeleteView, \
    PhoneContactDetailView, PhoneContactListView, PhoneContactUpdateView

from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView, TemplateView

urlpatterns = \
    patterns('',
             # Default
             url(r'^$', PhoneContactListView.as_view(), name="index"),

             # Contact
             url(r'^contact/list$', PhoneContactListView.as_view(), name="contact_list"),
             url(r'^contact/create/$', PhoneContactCreateView.as_view(), name="contact_create"),
             url(r'^contact/(?P<pk>[0-9]+)/$', PhoneContactDetailView.as_view(), name="contact"),
             url(r'^contact/(?P<pk>[0-9]+)/delete/$', PhoneContactDeleteView.as_view(), name="contact_delete"),
             url(r'^contact/(?P<pk>[0-9]+)/update/$', PhoneContactUpdateView.as_view(), name="contact_update"),

             # Address
             url(r'^address/list/$', PhoneAddressListView.as_view(), name="address_list"),
             url(r'^address/create/$', PhoneAddressCreateView.as_view(), name="address_create"),
             url(r'^address/(?P<pk>[0-9]+)/$', PhoneAddressDetailView.as_view(), name="address"),
             url(r'^address/(?P<pk>[0-9]+)/delete/$', PhoneAddressDeleteView.as_view(), name="address_delete"),
             url(r'^address/(?P<pk>[0-9]+)/update/$', PhoneAddressUpdateView.as_view(), name="address_update"),

             url(r'^redirect/$', RedirectView.as_view(url='http://djangoproject.com'), name='redirect_view'),
             url(r'^about/$', TemplateView.as_view(template_name="viewsintroduction/about.html"), name="template_view")
             )
