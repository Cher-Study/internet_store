from django.shortcuts import render
from authapp.models import ShopUser


def user_create(request):
    pass


def users(request):
    users = ShopUser.objects.all().order_by('id')

    return render(request, 'adminapp/user/users.html', context={
        'title': 'Пользователи',
        'objects': users,
    })


def user_update(request):
    pass


def user_delete(request):
    pass
