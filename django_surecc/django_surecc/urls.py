from django.conf.urls import patterns, include, url
# from django.conf.urls.defaults import *
from django_surecc.views import hello, current_datetime, hours_ahead, current_datetime_t_outer, current_datetime_t_rtr, display_meta, display_meta_t_rtr

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_surecc.views.home', name='home'),
    # url(r'^django_surecc/', include('django_surecc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # my website
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^timet/$', current_datetime_t_outer),
    url(r'^timetshortcut/$', current_datetime_t_rtr),
    # show request.META
    url(r'^meta/$', display_meta),
    url(r'^metat', display_meta_t_rtr),
)
