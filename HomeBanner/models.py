from django.db import models
from utils.models import BaseModel
import django.utils.timezone as timezone
# from django.contrib.postgres.fields import JSONField


# Create your models here.

class HomeBanner(BaseModel):
    class Meta:
        ordering = ['-sort']
        db_table = "home_banner"

    describe = models.CharField('描述', max_length=255)
    show_time = models.DateTimeField('显示时间', default=timezone.now, blank=True, null=True)
    hide_time = models.DateTimeField('下架时间', blank=True, null=True)
    banner_h5 = models.ImageField('Banner H5', blank=True, null=True)
    banner_pc = models.ImageField('Banner PC', blank=True, null=True)
    script_h5 = models.TextField('链接/脚本(h5)', blank=True, null=True)
    script_pc = models.TextField('链接/脚本(pc)', blank=True, null=True)
    sort = models.IntegerField('排序', default=1)
    # json_field = JSONField('JSON字段', db_index=True)
