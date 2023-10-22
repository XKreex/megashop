from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render
from django.template.defaultfilters import slugify

menu = ["О сайте", "Добавить", "Обратная связь", "Войти"]

data_db = [
    {'id': 1, 'title': 'i3-10300', 'content': 'processor 10 pokoleniya', 'in_stock': True},
    {'id': 2, 'title': 'i5-12500', 'content': 'processor 12 pokoleniya', 'in_stock': False},
    {'id': 3, 'title': 'i7-13700', 'content': 'processor 13 pokoleniya', 'in_stock': True},
]

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'megazzz/index.html', context=data)

def products(request):
    return render(request, 'megazzz/products.html', {'title': 'Каталог магазина'})

def categories(request, cat_id):
    return HttpResponse(f"<h1>ПРОЦЕССОРЫ</h1><p>id: {cat_id}</p>")

def categories_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>ПРОЦЕССОРЫ</h1><p>slug: {cat_slug}</p>")

#def archive(request, year):
#    if year > 2023:
#        uri = reverse('cats', args=('sports',))
#        return redirect(uri)
#    return HttpResponse(f"<h1>Поколение процессоров</h1><p>{year}</p>")

def radio(request):
    return HttpResponse(f"<h1>RadioTapok</h1>")

def archive(request, year):
    if year > 2023:
        uri = reverse('single', kwargs={'a1': 'music', 'a2': 'radio'})
        return redirect(uri)
    return HttpResponse(f"<h1>Поколение процессоров</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound ('<h1>СТАНИЦА НЕ НАЙДЕНА</h1>')

