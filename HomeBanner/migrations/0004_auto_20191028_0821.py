# Generated by Django 2.2.1 on 2019-10-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeBanner', '0003_auto_20191016_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homebanner',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='homebanner',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
