from django.conf.urls import patterns, include, url
# from django.conf.urls.defaults import *
from django_surecc.views import hello, current_datetime, hours_ahead, current_datetime_t_outer, current_datetime_t_rtr

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_surecc.views.home', name='home'),
    # url(r'^django_surecc/', include('django_surecc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^timetmplt/$', current_datetime_t_outer),
    (r'^timeshortcut/$', current_datetime_t_rtr),
)
