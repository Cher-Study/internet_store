from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Create your models here.


def get_activation_key_expiration_date():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    avatar = models.ImageField(
        verbose_name='аватар', blank=True, upload_to='users')
    phone = models.CharField(verbose_name='телефон', max_length=20, blank=True)
    city = models.CharField(verbose_name='город', max_length=20, blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(
        default=get_activation_key_expiration_date)
