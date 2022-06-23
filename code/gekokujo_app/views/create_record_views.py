from django.shortcuts import render
from django.http import HttpResponse
from ..forms import RecordsForm

# 成績入力フォーム


def createRecord(request):
    recordsform = RecordsForm()
    context = {
        'RecordsForm': recordsform
    }
    return render(request, 'create.html', context)
