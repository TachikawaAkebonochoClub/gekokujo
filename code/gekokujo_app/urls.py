from django.urls import path
from .views import *

urlpatterns = [
    # ランキング一覧
    path('', ranking_views.showRecords, name='showRecords'),
    # 成長記録
    path('history', history_views.showHistory, name='showHistory'),
    # 成績入力フォーム
    path('create', create_record_views.createRecord, name='createRecord'),
    # 成績登録処理
    path('add', add_record_views.addRecord, name='addRecord')
]
