from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo
from .forms import UserForm
from django.shortcuts import get_object_or_404

# ユーザー情報を辞書に格納してusers.htmlに返す
def showUsers(request):
    userinfo = UserInfo.objects.all()
    context = {
        'userinfo': userinfo,
        'count':userinfo.count,
    }
    return render(request, 'myapp/users.html',context)

# URLから受け取ったidの詳細情報をdetail.htmlに返す
def showDetail(request,id):
    userinfoDetail = get_object_or_404(UserInfo,pk=id)
    context = {
        'userinfoDetail':userinfoDetail,
    }
    return render(request,'myapp/detail.html',context)

# 編集フォームを返す
def showEditUserForm(request,id):
    userinfo = get_object_or_404(UserInfo,pk=id)
    userForm = UserForm(instance=userinfo)
    context = {
        'userinfo':userinfo,
        'userForm':userForm,
    }
    return render(request,'myapp/edit.html',context)

# フォームから受取ったデータでDBを更新する
def updateUser(request,id):
    #リクエストがPOSTの場合
    if request.method == 'POST':
        userInfo = get_object_or_404(UserInfo,pk=id)
        userForm = UserForm(request.POST,instance=userInfo)
        if userForm.is_valid():
            userForm.save()

    #更新後、対象ユーザの情報を表示
    userInfo = get_object_or_404(UserInfo,pk=id)
    context = {
        'userinfoDetail': userInfo,
    }
    return render(request, 'myapp/detail.html',context)

# 新規登録フォーム
def showCreateUserForm(request):
    form = UserForm()
    context = {
        'userForm':form,
    }
    return render(request, 'myapp/create.html',context)

# フォームから受取ったデータをDBに登録する
def addUser(request):
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            userForm.save()
    #登録後、全件データを抽出
    userinfo = UserInfo.objects.all()
    context = {
        'userinfo': userinfo,
        'count':userinfo.count,
    }
    return render(request, 'myapp/users.html',context)

# レコードを削除する
def deleteUser(request,id):
    UserInfo.objects.filter(id=id).delete()
    userinfo = UserInfo.objects.all()
    context = {
        'userinfo': userinfo,
        'count':userinfo.count,
    }
    return render(request, 'myapp/users.html',context)
