from django.contrib import admin
from .models import History
from django.http import StreamingHttpResponse
from django.core import serializers
import zipfile
import os
import json
from FrontEndTool.settings import BASE_DIR
from django import forms


# HistroyExport.short_description = "导出数据"
@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('gameName', 'gameID', 'name', 'platform', 'bet', 'awards', 'awardTime', 'isXiqi', 'isH5', 'banner')
    search_fields = ('gameName', 'gameID')
    actions = ['HistroyExport']

    def HistroyExport(self, request, queryset):
        # allHistory = History.objects.all().order_by('-awardTime')
        # years = History.objects.raw(
        #     u"SELECT strftime('%%Y',awardTime) as year,MAX(id) as id FROM BigAwardsHistory_history GROUP by year ORDER BY year DESC")

        dataObj = {'bigWin': {}, 'xiqi': {}}

        bigWinYears = History.objects.raw(
            u"SELECT strftime('%%Y',awardTime) as year,MAX(id) as id FROM bigwin_history WHERE isXiqi=0 GROUP by year ORDER BY year DESC")

        for bigWinYear in bigWinYears:
            dataObj['bigWin'][bigWinYear.year] = []
            result = History.objects.all().filter(awardTime__year=int(bigWinYear.year)).filter(isXiqi=False).order_by(
                '-awardTime')
            print(result)
            for history in result:
                dataObj['bigWin'][bigWinYear.year].append(history.toJSON())

        xiqiYears = History.objects.raw(
            u"SELECT strftime('%%Y',awardTime) as year,MAX(id) as id FROM bigwin_history WHERE isXiqi=1 GROUP by year ORDER BY year DESC")

        for xiqiYear in xiqiYears:
            dataObj['xiqi'][xiqiYear.year] = []
            result = History.objects.all().filter(awardTime__year=int(xiqiYear.year)).filter(isXiqi=True).order_by(
                '-awardTime')
            for history in result:
                dataObj['xiqi'][xiqiYear.year].append(history.toJSON())

        # 计算总获奖金额

        total = History.objects.raw('SELECT SUM(awards) as total,MAX(id) as id FROM bigwin_history');

        for t in total:
            dataObj['total'] = round(t.total, 2)

        # 将json保存为文件
        with open("BigWinData.json", "w") as f:
            f.write(json.dumps(dataObj, ensure_ascii=False))
        # zip打包img和json文件
        try:
            import zlib
            compression = zipfile.ZIP_DEFLATED
        except:
            compression = zipfile.ZIP_STORED
        f = zipfile.ZipFile('BigWinData.zip', 'w', compression)
        startdir = os.path.join(BASE_DIR, 'static/media/')
        allHistory = History.objects.all()
        for his in allHistory:
            filename = str(his.banner)
            f.write(os.path.join(startdir, filename), filename)
        # for dirpath, dirnames, filenames in os.walk(startdir):
        #     for filename in filenames:
        #         f.write(os.path.join(dirpath, filename), 'bigWinImgs/' + filename)
        f.write('BigWinData.json')
        f.close()

        def file_iterator(filename, chunk_size=512):
            with open(filename, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break

        response = StreamingHttpResponse(file_iterator('BigWinData.zip'))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename="{}" '.format("BigWinData.zip")

        # 返回zip包
        return response
        # for item in queryset:
        #     print(item)
        # pass

    HistroyExport.short_description = '导出数据'
# admin.site.register(History, HistoryAdmin)
