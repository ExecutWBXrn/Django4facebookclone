from django import template
import facebookcat.views as views

register = template.Library()

@register.simple_tag(name="cat")
def Category():
    return views.cat_db

@register.simple_tag(name="menu")
def menu():
    mainmenu = [
        {"title":"home", "url": "home"},
        {"title": "about site", "url": "about"},
        {"title": "publish photo", "url": "photo"},
        {"title": "about us", "url": "finfo"},
        {"title": "log in", "url": "log"},
        {"title": "categories", "url":"cat"},

    ]
    return mainmenu