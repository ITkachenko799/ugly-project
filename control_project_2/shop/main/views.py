from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    return render(request,'home.html')


def product(request):
    if request.method == "POST":
        current_id = request.POST.get('id', None)
        product = get_object_or_404(pk=current_id, klass=Prod)
        product.delete()
        product_list = Prod.objects.all()
    else:
        product_list = Prod.objects.all()

    paginator = Paginator(product_list, 4)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'product.html', {'product_list': product_list, 'page_obj': page_obj})


def products1_info(request):
    all_product = Prod.objects.all()

    return render(request, 'products_info.html', {'all_product': all_product[0:1]})


def products2_info(request):
    all_product = Prod.objects.all()

    return render(request, 'products_info2.html', {'all_product': all_product[1:2]})



