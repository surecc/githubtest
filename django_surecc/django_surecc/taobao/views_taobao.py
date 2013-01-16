# Create your views here.
from django.shortcuts import render_to_response
from django.http import  HttpResponse, HttpResponseRedirect
from django_surecc.taobao.forms import SoupForm
from django_surecc.taobao.models import *
# tool functions
from django_surecc.tools import getRandom, getHtml, getResource, taobao_lib, saveImg

def getsoup_old(request):
    return HttpResponse('i will think about it. i mean get soup.')

def show_soup_result(request):
    return HttpResponse('i have already done! Thanks!')

import os.path
import json
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
            path_img = os.path.join(os.path.join(os.path.dirname(__file__)), '..\\imgdb\\taobao_' + rd + '.jpg')
            localfile = os.path.join(os.path.join(os.path.dirname(__file__)), '..\\imgdb\\url_' + rd + '.txt')
            #getHtml.grabHref(url, localfile)
            #getResource.grabHref(url, localfile)
            #getResource.grab_360buy(url, localfile)
            #getResource.grab_360buy_saveToModel(url, 1, 1, localfile)
            data = taobao_lib.get_json(url)
            json_data = json.loads(data)
            json.loads(data, None)
            json_item_list = json_data['itemList']
            for item in json_item_list:
                price = item['currentPrice']
                name = item['fullTitle']
                url = item['storeLink']
                img_url = item['image']
                #save img
                saveImg.saveImg(img_url, path_img)
                
                #print name + price + url + img_url
            return render_to_response('beautiful_soup.html',{'form': form, 'ans':rd})
    else:
        form = SoupForm(initial={'url':'http://www.baidu.com'})
    return render_to_response('beautiful_soup.html',{'form': form})







