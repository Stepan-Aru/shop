from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import *


class ShopHome(ListView):
    paginate_by = 3
    model = Shop
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Shop.objects.filter(is_sale=True)


class ShopCats(ListView):
    model = Shop
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Shop.objects.filter(cat__slug=self.kwargs['cat_slug'], is_sale=True)


class ShowProduct(DetailView):
    model = Shop
    template_name = 'shop/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
