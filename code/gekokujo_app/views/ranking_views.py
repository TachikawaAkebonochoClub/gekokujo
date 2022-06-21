from django.shortcuts import render
from django.http import HttpResponse
from ..models import ScoreTable

# イニシャルとスコアを辞書に格納してrecords.htmlに返す

RAW_SQL = """
         SELECT A.*
            FROM gekokujo_app_scoretable A,
                (SELECT user_id ,max(score) score FROM gekokujo_app_scoretable GROUP BY user_id)B
            WHERE A.user_id = B.user_id and A.score = B.score
            ORDER BY A.score DESC;
"""

def showRecords(request):
    records_query_set = ScoreTable.objects.raw(RAW_SQL)

    records = []
    scr = 0
    rank = 0
    same_rank = 0

    for record in records_query_set:
        if scr != record.score:
            rank += 1 + same_rank
            scr = record.score
        elif scr == record.score:
            same_rank += 1
        records.append(
                {'rank': rank,
                'name': record.name,
                'score': record.score})
    context = {
        'scoretable': records
    }
    
    return render(request, 'records.html',context)
