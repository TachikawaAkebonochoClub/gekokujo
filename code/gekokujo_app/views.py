from django.shortcuts import render
from django.http import HttpResponse
from .models import ScoreTable

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
    return render(request, 'records.html',context)
