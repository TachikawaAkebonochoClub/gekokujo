from django.shortcuts import render
from django.http import HttpResponse
from .models import ScoreTable
from .forms import RecordsForm

# イニシャルとスコアを辞書に格納してrecords.htmlに返す

RAW_SQL = """
    SELECT ScoreTable.*
        FROM gekokujo_app_scoretable ScoreTable,
             (SELECT id , max(score) score FROM gekokujo_app_scoretable GROUP BY id) B
        WHERE ScoreTable.id = B.id 
          and ScoreTable.score = B.score
        ORDER BY ScoreTable.score DESC;
"""


def showRecords(request):
    records_query_set = ScoreTable.objects.raw(RAW_SQL)
    context = {
        'records': records_query_set,
        'count': len(records_query_set),
    }
    return render(request, 'records.html', context)

# 成績入力フォーム


def createRecord(request):
    recordsform = RecordsForm()
    context = {
        'RecordsForm': recordsform
    }
    return render(request, 'gekokujo_app/create.html', context)

# 成績登録処理


def addRecord(request):
    if request.method == 'POST':
        recordsform = RecordsForm(request.POST)
        if recordsform.is_valid():
            recordsform.save()
    scoretable = ScoreTable.objects.all()
    context = {
        'scoretable': scoretable,
        'count': scoretable.count,
    }
    return render(request, 'gekokujo_app/records.html', context)
