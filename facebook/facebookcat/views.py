from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    context = {
        "title" : "facebook.com",
    }
    return render(request, "facebookcat/index.html", context=context)

def about(request):
    context = {
        "title": "facebook.com",
    }
    return render(request, "facebookcat/about.html", context=context)

def nfound(request, exception):
    return HttpResponseNotFound("Not facebook")