from django.shortcuts import redirect
from django.http import HttpResponse
from ..models import ScoreTable
from ..forms import RecordsForm

# 成績登録処理


def addRecord(request):
    if request.method == 'POST':
        recordsform = RecordsForm(request.POST)
        if recordsform.is_valid():
            print('OK')
            recordsform.save()
        else:
            print(recordsform.errors.as_text())

    return redirect('showRecords')
    # shoeRecordsにリダイレクト
