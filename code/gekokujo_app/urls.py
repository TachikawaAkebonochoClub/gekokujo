from django.urls import path
from . import views

urlpatterns = [
   # ランキング一覧
   path('', views.showRecords, name='showRecords'),
   # 成長記録
   #path('history', views.showDetail, name='showDetail'),
   # 成績入力フォーム
   #path('create', views.createRecord, name='createRecord'),
   # 成績登録処理
   #path('add', views.addRecord, name='addRecord'), 
   ]
