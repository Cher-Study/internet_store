# Generated by Django 3.2.12 on 2022-02-20 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0004_auto_20220201_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'ordering': ('id',)},
        ),
    ]
