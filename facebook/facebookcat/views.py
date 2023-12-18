from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

db_data = [
    {"id":1, "photo":"some photo", "descripthion":"I'm took this photo when i'm clothing socks", "comments":"not comments below this photo yet", "is_published":True},
    {"id":2, "photo":"something photo", "descripthion":"zxc, dead inside, lubov pishla zivyali rosi, dota 2 > csgo", "comments":"not comments below this photo yet", "is_published":True},
    {"id":3, "photo":"photo some", "descripthion":"funny videos))) XD, pls subscribe and click on thumb up #cats #funny", "comments":"not comments below this photo yet", "is_published":True},
]
def index(request):
    context = {
        "title" : "facebook.com",
        "menu" : [
            {"title":"about site","url":"about"},
            {"title":"publish photo","url":"photo"},
            {"title":"about us","url":"finfo"},
            {"title":"log in","url":"log"},
        ],
        "DB_data" : db_data,
    }
    return render(request, "facebookcat/index.html", context=context)

def about(request):
    context = {
        "title" : "facebook.com",
    }
    return render(request, "facebookcat/about.html", context=context)

def photo(request):
    return HttpResponse("Here shall be photo")

def finfo(request):
    context={
        "title":"further information",
    }
    return render(request, "facebookcat/finfo.html", context=context)

def log(request):
    return HttpResponse("this page coming soon")

def nfound(request, exception):
    return HttpResponseNotFound("Not facebook")