from django.conf.urls import patterns, include, url
# from django.conf.urls.defaults import *
from django_surecc.views import views_01
from django_surecc.books import views_books 
from django_surecc.contact import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'django_surecc.views.home', name='home'),
    # url(r'^django_surecc/', include('django_surecc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # my website
    url(r'^hello/$', views_01.hello),
    url(r'^time/$', views_01.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views_01.hours_ahead),
    url(r'^timet/$', views_01.current_datetime_t_outer),
    url(r'^timetshortcut/$', views_01.current_datetime_t_rtr),
    # show request.META
    url(r'^meta/$', views_01.display_meta),
    url(r'^metat', views_01.display_meta_t_rtr),
    # Form:search a book
    url(r'^search-form/$', views_books.search_form),
    url(r'^search/$', views_books.search),
    url(r'^contact/$', views.contact),
)
