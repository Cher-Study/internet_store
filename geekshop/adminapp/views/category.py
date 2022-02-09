from django.shortcuts import render
from mainapp.models import ProductCategory
from adminapp.utils import superuser_required


@superuser_required
def category_create(request):
    pass


@superuser_required
def categories(request):
    categories = ProductCategory.objects.all().order_by('id')

    return render(request, 'adminapp/category/categories.html', context={
        'title': 'Категории',
        'objects': categories,
    })


@superuser_required
def category_update(request):
    pass


@superuser_required
def category_delete(request):
    pass