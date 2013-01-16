'''
Created on Jan 16, 2013

@author: surecc
'''
#grab the Taobao: title|price|url|img
from bs4 import BeautifulSoup
import urllib2
import os.path
# the model of taobao
from django_surecc.taobao import *
from django_surecc.tools import saveImg

def grab_360buy(url, localfile):
    request = urllib2.Request(url=url, headers={'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3' })
    response = urllib2.urlopen(request)
    HTML_response = response.read()
    soup = BeautifulSoup(HTML_response)
    if soup:
        tag_div = soup.find_all('div', id = 'plist')
        if tag_div:
            tag_item_li = tag_div[0].find_all('li')
            myfile = open(localfile,'w')
            i = 0
            for li in tag_item_li:
                i += 1
                #get the tag of each div
                div = li.find_all('div')
                if div:
                    print str(i)+'........'
                    p_img = div[0]
                    p_name = div[4]
                    p_price = div[5]
                    #save img
                    url_img = p_img.img['data-lazyload']
                    path_dir = os.path.join(os.path.dirname(localfile), 'img')
                    path_img = os.path.join(path_dir , str(i)+'.jpg')
                    saveImg.saveImg(url_img, path_img)
                    #save price
                    url_price = p_price.img['data-lazyload']
                    path_price = os.path.join(path_dir, str(i)+'_price.jpg')
                    saveImg.saveImg(url_price, path_price)
                    #get info
                    myfile.write( str(path_img) + '---')
                    myfile.write( str(p_name.a.contents) + '---')
                    myfile.write( str(p_price.img['data-lazyload']) + '---')
                    myfile.write('\r\n')
                else:
                    print 'it is empty of div.... fuck'
            myfile.close()
    return True
                    
#grab the urls with user-agent
def grabHref(url, localfile):
    request = urllib2.Request(url=url, 
                              headers={ 
                                       'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3',
                                       'Host' : 'list.taobao.com',
                                       'X-Requested-With' : 'XMLHttpRequest',
                                       'Accept' : 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
                                        })
    response = urllib2.urlopen(request)
    HTML_response = response.read()
    soup = BeautifulSoup(HTML_response)
    if HTML_response:
        myfile = open(localfile,'w')
        myfile.write(HTML_response)
        myfile.close()
    else:
        print 'it is empty here! Shit.............'
        
    '''
    content_li = soup.find_all('li', 'list-item list-item-grid')
    if not content_li:
        print 'it is empty here! Shit.............'
    else:
        myfile = open(localfile,'w')
        m_taobao = models.Commidity()
        list = []
        # get info 
        for item_li in content_li:
            # debug
            print item_li
            #tag_li = item_li.li
            tag_img = item_li.img
            tag_good = item_li.findAll('li', class_ = 'attr-price')
            if tag_good:
                tag_price = tag_good.span.strong.contents
            if tag_img:
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
                #print m_taobao
                # make a list
                list.append(m_taobao)
        myfile.close()
        '''
    return True

#grab the urls of website and save into localfile
def grabHref_old(url, localfile):
    # url local
    '''
    url = "F:\\MyProjects\\GitHub\\githubtest_old\\django_surecc\\sample_html\\taobao.htm"
    soup = BeautifulSoup(open(url))
    '''
    
    # url internet
    html = urllib2.urlopen(url).read()
    html = unicode(html,'gb2312','ignore').encode('utf-8','ignore')
    #html_ = html.replace('-','_')
    #print html_
    soup = BeautifulSoup(html)
    #print soup
    content_li = soup.find('a')
    print content_li
    
    if not content_li:
        print 'it is empty here! fuck..............'
    else:
        myfile = open(localfile, 'w')
        # list for the page
        m_taobao = models.Commidity()
        list = []
        # get info 
        for item_li in content_li:
            # debug
            print item_li
            #tag_li = item_li.li
            tag_img = item_li.img
            tag_good = item_li.findAll('li', class_ = 'attr-price')
            if tag_good:
                tag_price = tag_good.span.strong.contents
            if tag_img:
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
                #print m_taobao
                # make a list
                list.append(m_taobao)
        myfile.close()
    return True
    #return localfile