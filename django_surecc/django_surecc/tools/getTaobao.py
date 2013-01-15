'''
Created on Jan 16, 2013

@author: surecc
'''
#grab the Taobao: title|price|url|img
from bs4 import BeautifulSoup 
import urllib2
import re
# the model of taobao
from django_surecc.taobao import models

#grab the urls of website and save into localfile
def grabHref(url, localfile):
    #soup = BeautifulSoup(open(url))
    html = urllib2.urlopen(url).read()
    html = unicode(html,'gb2312','ignore').encode('utf-8','ignore')
    soup = BeautifulSoup(html)
    content_li = soup.find_all("li", class_ = "list-item list-item-grid")
    
    myfile = open(localfile, 'w')
    # list for the page
    list = []
    # get info 
    m_taobao = models.Commidity()
    for item_li in content_li:
        # debug
        print item_li
        #tag_li = item_li.li
        tag_img = item_li.img
        tag_price = item_li.findAll('li', class_ = 'attr-price').span.strong.contents
        #get the url of the img
        url_download_img = tag_img['src']
        #get url
        m_taobao.url = item_li['data-item']
        m_taobao.name = tag_img['alt']
        m_taobao.price = float(tag_price)
        # for debug
        m_taobao.categories = 0
        m_taobao.sellers = 0
        # debug
        myfile.write(m_taobao)
        print m_taobao
        # make a list
        list.append(m_taobao)
    myfile.close()
    return list 
    #return localfile