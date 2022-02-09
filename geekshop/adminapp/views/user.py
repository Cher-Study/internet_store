from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from authapp.models import ShopUser
from adminapp.forms import ShopUserAdminForm
from adminapp.utils import superuser_required


@superuser_required
def user_create(request):
    if request.method == 'POST':
        create_form = ShopUserAdminForm(
            request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        create_form = ShopUserAdminForm()
    return render(request, 'adminapp/user/edit.html', context={
        'title': 'Создание пользователя',
        'form': create_form
    })


@superuser_required
def users(request):
    users = ShopUser.objects.all().order_by('id')

    return render(request, 'adminapp/user/users.html', context={
        'title': 'Пользователи',
        'objects': users,
    })


@superuser_required
def user_update(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminForm(
            request.POST, request.FILES, instance=user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        edit_form = ShopUserAdminForm(instance=user)
    return render(request, 'adminapp/user/edit.html', context={
        'title': 'Редактирование пользователя',
        'form': edit_form
    })


@superuser_required
def user_delete(request, pk):
    title = 'Удаление пользователя'

    user = get_object_or_404(ShopUser, pk=pk)
    
    if request.method == 'POST':
        #user.delete()
        #вместо удаления лучше сделаем неактивным
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {'title': title, 'user_to_delete': user}
    
    return render(request, 'adminapp/user/delete.html', content)