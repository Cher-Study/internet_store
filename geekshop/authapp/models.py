from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='возраст')
    avatar = models.ImageField(
        verbose_name='аватар', blank=True, upload_to='users')
    phone = models.CharField(verbose_name='телефон', max_length=20, blank=True)
    city = models.CharField(verbose_name='город', max_length=20, blank=True)
