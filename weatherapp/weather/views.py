from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render (request, 'index.html')

def blank(request):
    return HttpResponse('<h1>Page was blank found</h1>')

def weather(request):
    return HttpResponse('<h1>Page was weather found</h1>')

