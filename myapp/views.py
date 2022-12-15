from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create y views here.

def index(request):
	features = Feature.objects.all
	return render(request,'index.html', {'features' : features})




