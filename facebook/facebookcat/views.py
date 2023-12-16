from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("Facebook main page")

def nfound(request, exception):
    return HttpResponseNotFound("Not facebook")