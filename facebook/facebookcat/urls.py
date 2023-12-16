from .views import *
from django.urls import path, register_converter
from.converter import *

register_converter(lim4symbConverter, "lim4symb")

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
]