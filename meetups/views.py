from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# request will be called automatically when Django calls this function in urls.py in 'project folder'
def index(request):
    return HttpResponse("<h1> Hello </h1>")