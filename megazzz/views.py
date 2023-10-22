from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render

menu = ["О сайте", "Добавить", "Обратная связь", "Войти"]

def index(request):
    #t = render_to_string('megazzz/index.html')
    #return HttpResponse(t)
    data = {
        'title': 'Главная станица',
        'menu': menu,
        'float': 25.56,
        'lst': [1, 2, 'abf', True],
        'set': {1, 2, 3, 2, 5},
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

