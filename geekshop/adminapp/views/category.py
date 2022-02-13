from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from mainapp.models import ProductCategory
from adminapp.forms import ProductCategoryAdminForm
from adminapp.utils import superuser_required


class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category/edit.html'
    form_class = ProductCategoryAdminForm
    success_url = reverse_lazy('admin:categories')

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание категории'
        return context


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/category/categories.html'

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        return context


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category/edit.html'
    form_class = ProductCategoryAdminForm
    success_url = reverse_lazy('admin:categories')

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование категории'
        return context


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category/delete.html'
    success_url = reverse_lazy('admin:categories')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление категории'
        return context