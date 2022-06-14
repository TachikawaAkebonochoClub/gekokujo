from django.urls import path
from . import views

urlpatterns = [
    path('', views.showUsers, name='showUsers'),
    # ユーザーの詳細
    path('<int:id>', views.showDetail,name='showDetail'),
    # ユーザー情報の編集
    path('<int:id>/edit',views.showEditUserForm,name='showEditUserForm'),
    # ユーザー情報更新
    path('<int:id>/update', views.updateUser, name='updateUser'),
    # ユーザーの登録フォーム
    path('create', views.showCreateUserForm, name='showCreateUserForm'),
    # ユーザー登録処理
    path('add', views.addUser, name='addUser'),
    # ユーザーの削除
    path('<int:id>/delete', views.deleteUser, name='deleteUser'),
]
