from django import forms
from . models import ScoreTable


class RecordsForm(forms.ModelForm):
    model = ScoreTable
    fields = ('id', 'user_id', 'name', 'date', 'course',
              'score', 'level', 'time', 'count', 'miss', 'read', 'rate', 'weakness')
    labelds = {
        'id': 'record_id',
        'user_id': 'user_id',
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


class form(forms.RecordsForm):
    id = forms.IntegerField(required=True)
    user_id = forms.IntegerField(required=True, default=1,)
    name = forms.CharField(required=True, max_length=30)
    date = forms.DateField(required=True)
    course = forms.ChoiceField(equired=True,)
    score = forms.IntegerField(required=True)
    level = forms.CharField(required=True)
    time = forms.TimeInput(required=True, format='%M:%S.%f')
    count = forms.IntegerField(required=True)
    miss = forms.IntegerField(required=True)
    read = forms.DecimalField(required=True, max_digits=5, decimal_places=2)
    rate = forms.IntegerField(required=True, max_digits=5, decimal_places=2)
    weakness = forms.IntegerField(rempty_value=True, max_length=10)
