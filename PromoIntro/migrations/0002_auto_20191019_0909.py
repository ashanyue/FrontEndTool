# Generated by Django 2.2.4 on 2019-10-19 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PromoIntro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocategory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='promocategory',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
