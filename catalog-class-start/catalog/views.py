from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


def home(request):
    products = Product.objects.all()
    lines = []

    for product in products:
        lines.append(f'{product.name} — {product.price} ₽')

    text = '\n'.join(lines) or 'Товаров пока нет'
    return HttpResponse(text, content_type='text/plain; charset=utf-8')


def about(request):
    return HttpResponse(
        '<h1>О каталоге</h1>'
        '<p>Здесь будут товары и цены.</p>'
        '<a href="/">На главную</a>'
    )


def contacts(request):
    return HttpResponse(
        '<h1>Контакты</h1>'
        '<p>Автор: Тимур</p>'
        '<a href="/">На главную</a>'
    )