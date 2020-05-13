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
    data = Movie.objects.filter(duration__lte = minutes)

    #render html with data
    return render(request, "pages/index.html", {'data': data})
