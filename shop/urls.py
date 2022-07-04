from django.urls import path

from .views import *

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('category/<slug:cat_slug>/', ShopCats.as_view(), name='category'),
    path('product/<slug:product_slug>/', ShowProduct.as_view(), name='product'),

]
