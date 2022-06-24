from django.shortcuts import render
from django.http import HttpResponse
from ..models import ScoreTable
from django.conf import settings

# 指定user_idのレコードをhistry.htmlに返す

def showHistory(request):
    rookie = settings.ROOKIES_ID
    records_query_set = ScoreTable.objects.filter(user_id = rookie).order_by("date").reverse()
    context = {
        'scoretable': records_query_set
    }

    return render(request, 'history.html',context)
