from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('cats/music/radio/', views.radio, name='radio'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_slug, name='cats_s'),
    path("archive/<year4:year>/", views.archive, name='archive'),
    path('cats/<slug:a1>/<slug:a2>/', views.archive, name='single'),


]
