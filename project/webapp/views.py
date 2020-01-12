from django.shortcuts import render, redirect
import json

def landing(request):
    return render(request, "pages/landing.html")

def index(request):
    filter = request.GET.get('answer', '')
    
    #filter data here
    data = "data"
    
    return render(request, "pages/index.html", { 'data': data })


