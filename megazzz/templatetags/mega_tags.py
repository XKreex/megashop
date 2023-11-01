from django import template
import megazzz.views as views
from megazzz.models import Category

register = template.Library()


# @register.simple_tag(name='get_cats')
# def get_categories():
#    return views.cats_db

@register.inclusion_tag('megazzz/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
