from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from mainapp.models import Product, ProductCategory
from adminapp.utils import superuser_required
from django.utils.decorators import method_decorator
from adminapp.forms import ProductEditAdminForm, ProductCreateAdminForm


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product/edit.html'
    success_url = reverse_lazy('admin:categories')
    fields = (
        'category',
        'name',
        'price',
        'color',
        'description',
        'image',
        'quantity',
        )
    
    @method_decorator(superuser_required)
    def dispatch(self, request,*args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {
            'category': self.get_category()
        }

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.get_category()
        return context
    

class ProductsListView(ListView):
    model = Product
    template_name = 'adminapp/product/products.html'

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_initial(self):
        return {
            'category': self.get_category()
        }

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список товаров'
        context["category"] = self.get_category()
        return context


class ProductReadDetailsView(DetailView):
    model = Product
    template_name = 'adminapp/product/read.html'

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {
            'category': self.get_category()
        }

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукт/подробнее'
        context["category"] = self.get_category()
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product/edit.html'
    form_class = ProductEditAdminForm
    success_url = reverse_lazy('admin:categories')

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_initial(self):
        return {
            'category': self.get_category()
        }

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование товара'
        context["category"] = self.get_category()
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product/delete.html'
    success_url = reverse_lazy('admin:categories')
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление товара'
        return context
