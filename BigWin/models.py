from django.db import models
from FrontEndTool.models import BaseModel


class History(BaseModel):
    class Meta:
        db_table = 'bigwin_history'

    PLATFORM_CHOICE = (
        (12, "AG国际厅"),
        (27, "AE厅"),
        (9, "BBIN厅"),
        (30, "CQ9厅"),
        (21, "DT厅"),
        (23, "PP厅"),
        (24, "PS厅"),
        (15, "PT厅"),
        (26, "PT国际厅"),
        (35, "PT亚洲厅"),
        (31, "PNG厅"),
        (34, "NT厅"),
        (17, "MG国际厅"),
        (22, "SW厅"),
        (18, "TTG厅"),
    )

    gameName = models.CharField(u'游戏名称', max_length=256)
    gameID = models.CharField(u'游戏ID', null=True, blank=True, max_length=256)
    platform = models.IntegerField(u'平台', choices=PLATFORM_CHOICE, null=True, blank=True, default=1)
    bet = models.DecimalField(u'投注金额', max_digits=10, decimal_places=2)
    awards = models.DecimalField(u'爆奖金额', max_digits=19, decimal_places=2)
    awardTime = models.DateField(u'中奖时间')
    banner = models.ImageField(u'图片', upload_to='bigWinImgs', blank=True, null=True)
    isH5 = models.BooleanField(u'是否H5', default=False)
    isXiqi = models.BooleanField(u'是否红包', default=False)
    name = models.CharField(u'中奖用户名', max_length=20, default='')
    objects = models.Manager()

    def get_banner(self):
        if self.banner:
            return self.banner.name
        else:
            return ''

    def image_tag(self):
        from django.utils.html import format_html
        img_url = self.get_banner()
        if img_url:
            return format_html('<img src="{}" width="100"  />'.format(self.banner.url))
        else:
            return ""
        # return '<img src="%s" />' % escape(self.get_banner())
        # return ""

    image_tag.short_description = 'banner'
    image_tag.allow_tags = True


class Platform(BaseModel):
    class Meta:
        db_table = "platform"

    name = models.CharField("平台名称", max_length=255, null=True, blank=True)
