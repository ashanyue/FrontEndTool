# Generated by Django 2.2.1 on 2019-10-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SysCore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='isMaintenance',
            field=models.BooleanField(default=False, verbose_name='启用维护'),
        ),
    ]
