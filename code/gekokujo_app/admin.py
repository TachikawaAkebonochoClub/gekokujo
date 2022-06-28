from django.contrib import admin
from .models import ScoreTable

admin.site.site_header = '下剋上管理サイト'
admin.site.index_title = 'スコアデータ'

@admin.register(ScoreTable)
class ScoreTableAdmin(admin.ModelAdmin):
    pass
