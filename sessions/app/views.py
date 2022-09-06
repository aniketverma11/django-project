from doctest import REPORT_UDIFF
from turtle import title
from django.shortcuts import render

import requests

from .models import Products

def index(request):
    return render(request, "index.html")

def product(request):
    return render(request, "product.html")

def load_product(request):
    r =  requests.get("hhtps://fakestoreapi.com/products")
    for item in r.json():
        product = Products(
            title=item["title"],
            description=item["description"],
            price=item['price'],
            image_url=item['image']
        )
        product.save()

    return render(request, "index.html")


