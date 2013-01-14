'''
Created on Jan 13, 2013

@author: surecc
'''
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import  HttpResponse, Http404
import datetime

# first case #
def hello(request):
    return HttpResponse("Hello World")

# show the current time#
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# show the futrue time according to the offset time#
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    ## assert False
    # html = "In %s hour(s), it will be %s." % (offset, dt)
    # return HttpResponse(html)
    return render_to_response('hours_ahead.html',({'hour_offset': offset,'next_time': dt}))
    

# Template view out file#
def current_datetime_t_outer(request):
    now = datetime.datetime.now()
    t = get_template('current_date.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

# shortcut of 1.get template 2.render 3.return response
def current_datetime_t_rtr(request):
    now = datetime.datetime.now()
    return render_to_response('current_date.html', {'current_date': now})

## Try the Request Form
# show he request.META
def display_meta(request):
    values = request.META.items();
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
    
def display_meta_t_rtr(request):
    values = request.META.items();
    values.sort()
    return render_to_response('meta.html',{'values_list': values})