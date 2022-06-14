from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo

# ユーザー情報を辞書に格納してusers.htmlに返す
def showUsers(request):
    userinfo = UserInfo.objects.all()
    context = {
        'userinfo': userinfo,
        'count':userinfo.count,
    }
    return render(request, 'myapp/users.html',context)
