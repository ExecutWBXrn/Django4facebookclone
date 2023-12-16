from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return render(request, "facebookcat/index.html")

def about(request):
    return render(request, "facebookcat/about.html")

def nfound(request, exception):
    return HttpResponseNotFound("Not facebook")