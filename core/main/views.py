from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requests):
    return render(requests, 'dark.html')

def about(requests):
    return HttpResponse(
        'this is about view'
    )

def contact(requests):
    return HttpResponse(
        'this is contact view'
    )

def portfolio(requests):
    return HttpResponse(
        'this is portfolio view'
    )