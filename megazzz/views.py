from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return HttpResponse("Страница магазина Мегазон")

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

def radiorapok(request):
    return HttpResponse(f"<h1>RadioTapok</h1>")

def archive(request, year):
    if year > 2023:
        uri = reverse('single', kwargs={'a1': 'music', 'a2': 'radiotapok'})
        return redirect(uri)
    return HttpResponse(f"<h1>Поколение процессоров</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound ('<h1>СТАНИЦА НЕ НАЙДЕНА</h1>')

