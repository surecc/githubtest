# Create your views here.
from django.shortcuts import render_to_response
from django.http import  HttpResponse, HttpResponseRedirect
from django_surecc.taobao.forms import SoupForm
from django_surecc.taobao.models import *
# tool functions
from django_surecc.tools import getRandom

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
            ans = grabHref(url, localfile)
            #return HttpResponse('i have already write the href into %s': %(localfile))
            #return HttpResponseRedirect('/soup/result/')
            return render_to_response('beautiful_soup.html',{'form': form, 'ans':rd})
    else:
        form = SoupForm(initial={'url':'http://127.0.0.1:8000/admin/'})
    return render_to_response('beautiful_soup.html',{'form': form})


#grab the href
from bs4 import BeautifulSoup 
import urllib2
import re
#grab the urls of website and save into localfile
def grabHref(url, localfile):
    html = urllib2.urlopen(url).read()
    html = unicode(html,'gb2312','ignore').encode('utf-8','ignore')
    content = BeautifulSoup(html).findAll('a')
    myfile = open(localfile,'w')
    pat1 = re.compile(r'href="([^"]*)"')
    pat2 = re.compile(r'http')
    ans = ""
    for item in content:
        h = pat1.search(str(item))
        href = h.group(1)
        if pat2.search(href):
            ans = href
        else:
            ans = url+href
        myfile.write(ans)
        myfile.write('\r')
        print ans
    myfile.close()
    return ans 
    #return localfile