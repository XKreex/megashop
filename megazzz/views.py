from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render
from django.template.defaultfilters import slugify


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]

data_db = [
    {'id': 1, 'title': 'i3-10300', 'content': 'processor 10 pokoleniya', 'in_stock': True},
    {'id': 2, 'title': 'i5-12500', 'content': 'processor 12 pokoleniya', 'in_stock': False},
    {'id': 3, 'title': 'i7-13700', 'content': 'processor 13 pokoleniya', 'in_stock': True},
    {'id': 4, 'title': 'Gigabyte GeForce GTX 1660 SUPER', 'content': '''<h3>Видеокарта</h3> GIGABYTE Nvidia GeForce GTX 1660SUPER (GV-N166SD6-6GD) 6 ГБ
        Частота графического процессора, МГц 1830
        Макс. частота графического процессора (Boost), МГц 1830
        Число универсальных процессоров 1408
        Версия шейдеров 6.0
        Число текстурных блоков 88
        Число блоков растеризации 48''',
         'in_stock': True},
]

cats_db = [
    {'id': 1, 'name': 'Процессоры'},
    {'id': 2, 'name': 'Видеокарты'},
    {'id': 3, 'name': 'Материнские платы'},
]

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'megazzz/index.html', context=data)

def products(request):
    return render(request, 'megazzz/products.html', {'title': 'Каталог магазина'})


def show_post(request, post_id):
    return HttpResponse(f'Отображение описания с id = {post_id}')

def about(request):
    return render(request, 'megazzz/about.html', {'title': 'О сайте', 'menu': menu})

def addpage(request):
    return HttpResponse(f'Добавление статьи')

def contact(request):
    return HttpResponse(f'Обратная связь')

def login(request):
    return HttpResponse(f'Авторизация')

def show_category(request, cat_id):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'megazzz/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>СТАНИЦА НЕ НАЙДЕНА</h1>')


