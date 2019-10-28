from django.contrib import admin
from .models import HomeBanner


# Register your models here.
@admin.register(HomeBanner)
class PromoCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'describe', 'show_time', 'hide_time', 'banner_h5', 'script_h5',  'banner_pc', 'script_pc',
        'sort')
    search_fields = ('describe', 'show_time',)
