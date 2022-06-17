from django.shortcuts import render
from django.http import HttpResponse
from .models import ScoreTable

# イニシャルとスコアを辞書に格納してrecords.htmlに返す
def showRecords(request):
    sql = "SELECT A.name,A.score
           FROM ScoreTable A,
           (SELECT id , max(score) score
            FROM ScoreTable GROUP BY id)B
           WHERE A.id = B.id and A.score = B.score;"
    records_query_set = ScoreTable.objects.raw(sql)
    records_list = list(records_query_set.values())
    records_list = [
        {'name': 'A', 'score': 100}, 
        {'name': 'B', 'score': 200}
        ]
    ranking = []
    if len(records_list):
        scr = records_list['score']
        rank = 1
        for record in records_list:
            if scr != record['score']:
                rank += 1
                scr = record['score']
            rank_dic = {
                'rank': rank,
                'name': record.name, 
                'score': record.score
                }
            ranking.append(rank_dic)
    return ranking

    context = {
        'scoretable': ranking,
        'count':records_query_set.count,
    }
    return render(request, 'gekokujo_app.records.html',context)
