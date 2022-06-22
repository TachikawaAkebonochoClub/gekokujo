from django.shortcuts import render
from django.http import HttpResponse
from ..models import ScoreTable

# 指定user_idのレコードをhistry.htmlに返す

def showHistory(request):
    records_query_set = ScoreTable.objects.filter(user_id=1).order_by("date")
    context = {
        'scoretable': records_query_set
    }

    return render(request, 'history.html',context)
