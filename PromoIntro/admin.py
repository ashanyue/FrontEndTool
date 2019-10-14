from django.contrib import admin
from .models import PromoCategory, Promo
import json
import zipfile
import os
from FrontEndTool.settings import BASE_DIR
from django.http import StreamingHttpResponse


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time', 'sort', 'isExpired', 'link', 'get_categorys', 'banner')
    search_fields = ('title',)
    actions = ['PromoExport']

    def PromoExport(self, request, queryset):
        # 创建一个zip文件
        try:
            import zlib
            compression = zipfile.ZIP_DEFLATED
        except:
            compression = zipfile.ZIP_STORED
        zip_f = zipfile.ZipFile('PromoIntros.zip', 'w', compression)
        startdir = os.path.join(BASE_DIR, 'static/media/')
        listPromo = []

        for item in Promo.objects.all():
            intro_file_name = str( item.id) + ".json"
            dit_promo = {'title': item.title, 'time': item.time, 'banner': item.get_banner(),
                         'category': [c.code for c in item.category.all()], 'link': item.link, 'isDirect': item.isLink,
                         'id': item.id}
            listPromo.append(dit_promo)

            dit_intro = {'title': item.title, 'time': item.time, 'category': dit_promo['category'],
                         'content': item.content,'link': item.link}
            with open(intro_file_name, "w") as f:
                f.write(json.dumps(dit_intro, ensure_ascii=False))
            zip_f.write(intro_file_name)
            os.remove(intro_file_name)
            # 将图片装入zip
            if item.banner:
                zip_f.write(os.path.join(startdir, dit_promo['banner']), dit_promo['banner'])

        with open("PromoList.json", "w") as f:
            f.write(json.dumps(listPromo, ensure_ascii=False))

        print(listPromo)
        # PromoList.json 装入zip
        zip_f.write('PromoList.json')
        zip_f.close()
        os.remove('PromoList.json')

        def file_iterator(filename, chunk_size=512):
            with open(filename, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break

        response = StreamingHttpResponse(file_iterator('PromoIntros.zip'))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename="{}" '.format("PromoIntros.zip")

        # 返回zip包
        return response

    PromoExport.short_description = '导出数据'


@admin.register(PromoCategory)
class PromoCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'created', 'updated')
    search_fields = ('name',)