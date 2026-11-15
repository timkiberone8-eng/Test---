from django.http import HttpResponse

def home(request):
    return HttpResponse(
        '<h1>Каталог работает</h1>'
        '<a href="/about/">О каталоге</a><br>'
        '<a href="/contacts/">Контакты</a>'
    )

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