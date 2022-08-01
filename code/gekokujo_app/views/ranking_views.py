from optparse import Values
from django.shortcuts import render
from django.http import HttpResponse
from ..models import ScoreTable
from django.conf import settings
from django.db.models import Max, Min
from operator import itemgetter

################ コース選択用関数 ####################


def select():

    courses = {
        100: 'おやじギャグ',
        200: 'お嬢様ことば',
        300: '早口ことば',
        400: '回文',
        500: '缶コーヒーのコピー',
        600: '時代劇のセリフ',
        700: '元気が出ることば',
        800: 'アニメタイトル',
    }

    selectcourses = ScoreTable.objects.all().order_by(
        'course').distinct().values_list('course')

    courselist = []
    for n in selectcourses:
        for l in n:
            courselist.append(l)

    coursedic = {}
    for s in courselist:
        for k, v in courses.items():
            if k == s:
                dic = {
                    k: v
                }
                coursedic.update(dic)
    return coursedic

# コースに応じて順位付けした結果を返す


def showRecords(request):

    if request.POST:
        coursenum = request.POST["course"]
        if coursenum == '0':
            records_query_set = ScoreTable.objects.values('user_id').annotate(score_max=Max(
                'score'), date_min=Min('date')).order_by('score_max').reverse().values(*["user_id", "score_max", 'date_min'])
        else:
            records_query_set = ScoreTable.objects.filter(course=coursenum).values('user_id').annotate(score_max=Max(
                'score'), date_min=Min('date')).order_by('score_max').reverse().values(*["user_id", "score_max", 'date_min'])
    else:
        records_query_set = ScoreTable.objects.values('user_id').annotate(score_max=Max(
            'score')).order_by('score_max').reverse().values(*["user_id", "score_max"])

    set = ScoreTable.objects.values()

    set_list = []

    for r in records_query_set:
        for s in set:
            if r['user_id'] == s['user_id'] and r['score_max'] == s['score']:
                set_list.append(s)

    new_list = []
    d = 0

    for l in set_list:
        if d == 0:
            d = l
        elif d['user_id'] == l['user_id']:
            if d['date'] > l['date']:
                d = l
        elif d['user_id'] != l['user_id']:
            new_list.append(d)
            d = l
    new_list.append(d)

    records = []
    scr = 0
    rank = 0
    same_rank = 0

    for record in new_list:
        score = record["score"]

        if scr != score:
            rank += 1 + same_rank
            scr = score
            same_rank = 0
        elif scr == score:
            same_rank += 1
        records.append(
            {'rank': rank,
             'name': record["name"],
             'rookie': True if record["user_id"] == int(settings.ROOKIES_ID) else False,
             'level': record["level"],
             'score_max': score})

    context = {
        'scoretable': records,
        'course': select()
    }
    return render(request, 'records.html', context)

################### 以下以前のファイル ########################

# RAW_SQL = """
#           SELECT gekokujo_app_scoretable.* FROM gekokujo_app_scoretable,
#               (SELECT a.user_id, a.score, min(a.date) date
#                   FROM gekokujo_app_scoretable a,
#                       (SELECT user_id, max(score) score
#                           FROM gekokujo_app_scoretable
#                               GROUP BY user_id) b
#                       WHERE a.user_id = b.user_id
#                           and a.score = b.score
#                       GROUP BY a.user_id,a.score) y
#               WHERE gekokujo_app_scoretable.user_id = y.user_id
#                   and gekokujo_app_scoretable.score = y.score
#                   and gekokujo_app_scoretable.date = y.date
#               ORDER BY gekokujo_app_scoretable.score DESC;
# """


# def showRecords(request):
#     courses = {
#         100: 'おやじギャグ',
#         200: 'お嬢様ことば',
#         300: '早口ことば',
#         400: '回文',
#         500: '缶コーヒーのコピー',
#         600: '時代劇のセリフ',
#         700: '元気が出ることば',
#         800: 'アニメタイトル',
#     }

#     if request.POST:
#         coursenum = request.POST["course"]
#         if coursenum == '0':
#             records_query_set = ScoreTable.objects.values('user_id').annotate(score_max=Max(
#                 'score'), date_min=Min('date')).order_by('score_max').reverse().values(*["user_id", "score_max", 'date_min'])
#         else:
#             records_query_set = ScoreTable.objects.filter(course=coursenum).values('user_id').annotate(score_max=Max(
#                 'score'), date_min=Min('date')).order_by('score_max').reverse().values(*["user_id", "score_max", 'date_min'])
#     else:
#         records_query_set = ScoreTable.objects.values('user_id').annotate(score_max=Max(
#             'score'), date_min=Min('date')).order_by('score_max').reverse().values(*["user_id", "score_max", 'date_min'])

#     selectcourses = ScoreTable.objects.all().order_by(
#         'course').distinct().values_list('course')

#     courselist = []
#     for n in selectcourses:
#         for l in n:
#             courselist.append(l)

#     coursedic = {}
#     for s in courselist:
#         for k, v in courses.items():
#             if k == s:
#                 dic = {
#                     k: v
#                 }
#                 coursedic.update(dic)
#             # else:
#             #     dic = {
#             #         'test': 'error'
#             #     }
#             #     coursedic.update(dic)

#     print('---------')
#     print(records_query_set)
#     records = []
#     scr = 0
#     rank = 0
#     same_rank = 0

#     for record in records_query_set:
#         if scr != record.score_max:
#             rank += 1 + same_rank
#             scr = record.score_max
#         elif scr == record.score_max:
#             same_rank += 1
#         records.append(
#             {'rank': rank,
#              'name': record.name,
#              'rookie': True if record.user_id == int(settings.ROOKIES_ID) else False,
#              'level': record.level,
#              'score': record.score_max})
#     context = {
#         'scoretable': records,
#         'course': coursedic
#     }

#     # context = {
#     #     'scoretable': records_query_set,
#     #     'course': coursedic
#     # }

#     return render(request, 'records.html', context)

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
