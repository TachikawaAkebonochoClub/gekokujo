from django.shortcuts import render,redirect
from django.http import HttpResponse
from ..models import ScoreTable
from ..forms import RecordsForm

# 成績登録処理

# formから取得したデータをDBに保存し、ランキング一覧に戻る
def addRecord(request):
    if request.method == 'POST':
        recordsform = RecordsForm(request.POST)
        if not recordsform.is_valid():
            return render(request, 'save_error.html')
        else:
            recordsform.save()
            return redirect('showRecords')
