from django.db import models
from FrontEndTool.models import BaseModel
from ckeditor.fields import RichTextField


class PromoCategory(BaseModel):
    class Meta:
        db_table = "promo_category"

    name = models.CharField('类别名称', max_length=20)
    code = models.CharField('类别代码', max_length=20)

    def __str__(self):
        return self.name


class Promo(BaseModel):
    class Meta:
        ordering = ['-sort']
        db_table = "promo_item"

    title = models.CharField('标题', max_length=255)
    time = models.CharField('显示时间', max_length=255)
    content = RichTextField(blank=True, null=True)
    link = models.CharField('链接', max_length=255, blank=True, null=True)
    category = models.ManyToManyField("PromoCategory")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    banner = models.ImageField('图片', upload_to='promoIntro', blank=True, null=True)
    isLink = models.BooleanField(u'是否直接链接', default=False)
    isExpired = models.BooleanField(u'是否已过期', default=False)
    sort = models.IntegerField("排序", default=1)

    def get_categorys(self):
        return "，".join([p.name for p in self.category.all()])

    def get_banner(self):
        if self.banner:
            return self.banner.name
        else:
            return ''


