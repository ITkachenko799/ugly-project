from django.urls import path
from .views import *

urlpatterns = [
    path('', product, name='home'),
    path('products', product, name='products'),
    path('products_info', products1_info, name='info'),
    path('products_info2', products2_info, name='info2')
]


