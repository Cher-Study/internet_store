# Generated by Django 3.2.12 on 2022-03-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20220223_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='city',
            field=models.CharField(blank=True, max_length=64, verbose_name='город'),
        ),
    ]
