from django.shortcuts import render
from mainapp.models import ProductCategory


def category_create(request):
    pass


def categories(request):
    categories = ProductCategory.objects.all().order_by('id')

    return render(request, 'adminapp/category/categories.html', context={
        'title': 'Категории',
        'objects': categories,
    })


def category_update(request):
    pass


def category_delete(request):
    pass