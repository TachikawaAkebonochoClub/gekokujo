from django import forms
from . models import ScoreTable


class RecordsForm(forms.ModelForm):
    model = ScoreTable
    fields = ('id', 'name', 'date', 'course',
              'score', 'level', 'time', 'count', 'miss', 'read', 'rate', 'weakness')
    labelds = {
        'id': 'ID',
        'name': 'イニシャル',
        'date': '実施日',
        'course': 'コース',
        'score': 'スコア',
        'level': 'レベル',
        'time': '入力時間',
        'count': '入力文字数',
        'miss': 'ミス入力数',
        'read': 'WPM',
        'rate': '正確率',
        'weakness': '苦手キー',
    }
