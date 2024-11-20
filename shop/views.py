# shop/views.py

from django.shortcuts import render, get_object_or_404
from .models import Store, Product


def home(request):
    stores = Store.objects.all()
    return render(request, 'shop/home.html', {'stores': stores})


def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    top_products = Product.objects.filter(store=store, is_top_selling=True)
    sale_products = Product.objects.filter(store=store, is_on_sale=True)
    seasonal_products = Product.objects.filter(store=store, is_seasonal=True)

    return render(request, 'shop/store_detail.html', {
        'store': store,
        'top_products': top_products,
        'sale_products': sale_products,
        'seasonal_products': seasonal_products,
    })
