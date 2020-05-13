# import grequests
from django.shortcuts import render, redirect
import json
from .models import Movie

def landing(request):
    return render(request, "pages/landing.html")

def index(request):

    #get string val
    answer = request.GET.get('minutes', '')
    
    #convert to int
    minutes = int(answer)

    #filter data
    if minutes == 30:
        data = Movie.objects.filter(duration__lte = minutes)
    elif minutes == 40:
        data = Movie.objects.filter(duration__lte = minutes, duration__gt = 30)
    elif minutes == 60:
        data = Movie.objects.filter(duration__lte = minutes, duration__gt = 40)
    else: # minutes == 90
        data = Movie.objects.filter(duration__lte = minutes, duration__gt = 60) 

    #render html with data
    return render(request, "pages/index.html", {'data': data})
