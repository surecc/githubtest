'''
Created on Jan 14, 2013

@author: surecc
'''
from django.shortcuts import render_to_response

def search_form(request):
    return render_to_response('search_form.html')
