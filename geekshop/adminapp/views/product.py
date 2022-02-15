from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from mainapp.models import Product, ProductCategory
from adminapp.utils import superuser_required
from django.utils.decorators import method_decorator
from adminapp.forms import ProductEditAdminForm, ProductCreateAdminForm


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product/edit.html'
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

    def get_success_url(self) -> str:
        return reverse('admin:products', kwargs=self.kwargs)

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

# def products(request, pk):
#     title = 'админка/продукт'

#     category = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(pk=pk).order_by('name')

#     content = {
#         'title': title,
#         'category': category,
#         'objects': products_list,
#     }

#     return render(request, 'adminapp/product/products.html', content)


class ProductReadDetailsView(DetailView):
    model = Product
    template_name = 'adminapp/product/read.html'

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def get_initial(self):
    #     return {
    #         'category': self.get_category()
    #     }

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукт/подробнее'
        context["category"] = self.get_category()
        return context

def product_read(request, pk):
    title = 'продукт/подробнее'    
    product = get_object_or_404(Product, pk=pk)
    content = {'title': title, 'object': product,}
    
    return render(request, 'adminapp/product/read.html', content)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product/edit.html'
    form_class = ProductEditAdminForm

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    # def get_initial(self):
    #     return {
    #         'category': self.get_category()
    #     }
    
    def get_success_url(self) -> str:
        return reverse('admin:products', kwargs=self.kwargs)

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование товара'
        context["category"] = self.get_category()
        return context

# def product_update(request, pk):
#     title = 'продукт/редактирование'
       
#     edit_product = get_object_or_404(Product, pk=pk)
    
#     if request.method == 'POST':
#         edit_form = ProductEditAdminForm(request.POST, request.FILES, instance=edit_product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:product_update',\
#                                                  args=[edit_product.pk]))
#     else:
#         edit_form = ProductEditAdminForm(instance=edit_product)
    
#     content = {'title': title, 
#                'update_form': edit_form, 
#                'category': edit_product.category 
#     }
    
#     return render(request, 'adminapp/product/edit.html', content)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product/delete.html'
    # success_url = reverse_lazy('admin:categories')
    
    # def get_category(self):
    #     return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление товара'
        # context["category"] = self.get_category()
        return context
        

    def get_success_url(self) -> str:
        return reverse('admin:products', kwargs=self.kwargs)
