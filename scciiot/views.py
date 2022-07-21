

from django.http import HttpResponse

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Home Page')

def home(request):
    return render(request, 'home.html')