from django.shortcuts import render_to_response
from django.http import  HttpResponse
from django_surecc.books.models import Book

def search_form(request):
    return render_to_response('search_form.html')

#the simplest way to search
def search_try(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
 
#better way to search       
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', 
                                  {'books':books, 'query':q})
    return render_to_response('search_form.html',{'error':error})