from django.conf.urls import patterns, url

from .views import index, collections, dates, conditions, strings, numbers, extension, urls, includes, debug, \
    static_files

urlpatterns = \
    patterns('',
             url(r'^$', index, name="index"),
             url(r'^urls$', urls, name='urls'),
             url(r'^debug$', debug, name='debug'),
             url(r'^index$', index, name="index"),
             url(r'^dates$', dates, name='dates'),
             url(r'^strings$', strings, name='strings'),
             url(r'^numbers$', numbers, name='numbers'),
             url(r'^static$', static_files, name="static"),
             url(r'^includes$', includes, name='includes'),
             url(r'^extension$', extension, name='extension'),
             url(r'^conditions$', conditions, name='conditions'),
             url(r'^collections$', collections, name="collections")
             )
