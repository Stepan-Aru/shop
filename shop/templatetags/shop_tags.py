from django import template
from shop.models import *

register = template.Library()


@register.inclusion_tag('Shop/menu.html')
def show_menu():
    cats = Category.objects.all()
    return {'cats': cats}