from django.conf.urls import patterns, include, url
# from django.conf.urls.defaults import *
from django_surecc.views import hello, current_datetime

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
    ('^hello/$', hello),
    ('^time/$', current_datetime),
)
