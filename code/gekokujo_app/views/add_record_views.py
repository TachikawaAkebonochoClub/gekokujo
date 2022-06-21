from django.shortcuts import render
from django.http import HttpResponse
from ..models import ScoreTable
from ..forms import RecordsForm

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
