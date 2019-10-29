# Generated by Django 2.2.1 on 2019-10-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigWin', '0003_merge_20191028_0816'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Platform',
        ),
        migrations.AlterField(
            model_name='history',
            name='platform',
            field=models.IntegerField(blank=True, choices=[(12, 'AG国际厅'), (27, 'AE厅'), (9, 'BBIN厅'), (30, 'CQ9厅'), (21, 'DT厅'), (23, 'PP厅'), (24, 'PS厅'), (15, 'PT厅'), (26, 'PT国际厅'), (35, 'PT亚洲厅'), (31, 'PNG厅'), (34, 'NT厅'), (17, 'MG国际厅'), (22, 'SW厅'), (18, 'TTG厅'), (37, 'MG亚洲厅')], default=1, null=True, verbose_name='平台'),
        ),
    ]