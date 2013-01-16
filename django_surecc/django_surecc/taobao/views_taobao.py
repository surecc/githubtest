# Create your views here.
from django.shortcuts import render_to_response
from django.http import  HttpResponse, HttpResponseRedirect
from django_surecc.taobao.forms import SoupForm
from django_surecc.taobao.models import *
# tool functions
from django_surecc.tools import getRandom, getHtml, getResource

def getsoup_old(request):
    return HttpResponse('i will think about it. i mean get soup.')

def show_soup_result(request):
    return HttpResponse('i have already done! Thanks!')

import os.path
#from django_surecc.conf import surecc
def getsoup(request):
    if request.method == 'POST':
        form = SoupForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            # as below, will grab the data of the url
            url = clean_data['url']
            # store the url into a file named try.txt
            #rd = getRandomStr(10)
            #rd = getRandom.getRandomStr(10)
            rd = getRandom.getUUID()
            # os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
            localfile = os.path.join(os.path.join(os.path.dirname(__file__)), '..\\imgdb\\url_' + rd + '.txt')
            #getHtml.grabHref(url, localfile)
            #getResource.grabHref(url, localfile)
            getResource.grab_360buy(url, localfile)
            #return HttpResponse('i have already write the href into %s': %(localfile))
            #return HttpResponseRedirect('/soup/result/')
            return render_to_response('beautiful_soup.html',{'form': form, 'ans':rd})
    else:
        form = SoupForm(initial={'url':'http://www.baidu.com'})
    return render_to_response('beautiful_soup.html',{'form': form})
