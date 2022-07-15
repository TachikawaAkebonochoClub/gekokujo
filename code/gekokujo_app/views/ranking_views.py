from optparse import Values
from django.shortcuts import render
from django.http import HttpResponse
from ..models import ScoreTable
from django.conf import settings
from django.db.models import Max, Min

# ランキングを生成してrecords.htmlに返す

RAW_SQL = """
          SELECT gekokujo_app_scoretable.* FROM gekokujo_app_scoretable,
              (SELECT a.user_id, a.score, min(a.date) date
                  FROM gekokujo_app_scoretable a,
                      (SELECT user_id, max(score) score
                          FROM gekokujo_app_scoretable
                              GROUP BY user_id) b
                      WHERE a.user_id = b.user_id
                          and a.score = b.score
                      GROUP BY a.user_id,a.score) y
              WHERE gekokujo_app_scoretable.user_id = y.user_id
                  and gekokujo_app_scoretable.score = y.score
                  and gekokujo_app_scoretable.date = y.date
              ORDER BY gekokujo_app_scoretable.score DESC;
"""


def showRecords(request):

    records = ScoreTable.objects.filter(course='').values('user_id').annotate(score_max=Max(
        'score'), date_min=Min('date')).order_by('score_max').reverse().values(*["user_id", "score_max", 'date_min'])
    context = {
        'scoretable': records
    }

# def showRecords(request):
    # records_query_set = ScoreTable.objects.raw(RAW_SQL)

    # records = []
    # scr = 0
    # rank = 0
    # same_rank = 0

    # for record in records_query_set:
    #     if scr != record.score:
    #         rank += 1 + same_rank
    #         scr = record.score
    #     elif scr == record.score:
    #         same_rank += 1
    #     records.append(
    #         {'rank': rank,
    #          'name': record.name,
    #          'rookie': True if record.user_id == int(settings.ROOKIES_ID) else False,
    #          'level': record.level,
    #          'score': record.score})
    # context = {
    #     'scoretable': records
    # }

    return render(request, 'records.html', context)
