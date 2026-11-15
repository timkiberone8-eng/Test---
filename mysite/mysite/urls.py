from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from catalog.views import home


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


urlpatterns = [
    path('', home),
    path('about/', about),
    path('contacts/', contacts),
    path('admin/', admin.site.urls),
]
