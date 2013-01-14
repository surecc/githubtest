from django.shortcuts import render_to_response
from django.http import  HttpResponse
from django_surecc.books.models import Book

def search_form(request):
    return render_to_response('search_form.html')

def search_try(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
        
def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html', 
                                  {'books':books, 'query':q})
    else:
        return HttpResponse('Please submit a search term.')