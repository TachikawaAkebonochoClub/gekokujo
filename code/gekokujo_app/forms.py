from django import forms
from .models import ScoreTable


class RecordsForm(forms.ModelForm):
    class Meta:
        model = ScoreTable
        fields = ('user_id', 'name', 'date', 'course',
                  'score', 'level', 'time', 'count', 'miss', 'read', 'rate', 'weakness')
        labelds = {
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
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '山田太郎の場合→T.Y'}),
            'score': forms.TextInput(attrs={'placeholder': 'スコアを入力してください'}),
            'level': forms.TextInput(attrs={'placeholder': 'レベルを入力してください'}),
            'time': forms.TextInput(attrs={'placeholder': '時:分:秒.ミリ秒で入力してください'}),
            'count': forms.TextInput(attrs={'placeholder': '入力文字数を入力してください'}),
            'miss': forms.TextInput(attrs={'placeholder': 'ミス入力数を入力してください'}),
            'read': forms.TextInput(attrs={'placeholder': 'WPMを入力してください'}),
            'rate': forms.TextInput(attrs={'placeholder': '正確率を入力してください'}),
            'weakness': forms.TextInput(attrs={'placeholder': '苦手キーを入力してください'}),
        }

    #     error_messages = {
    #         'user_id': {
    #             'required': 'user_idが入力されていません'
    #         },
    #         'name': {
    #             'required': 'イニシャルが入力されていません'
    #         },
    #         'date': {
    #             'required': '実施日が入力されていません'
    #         },
    #         'course': {
    #             'required': 'コースが入力されていません'
    #         },
    #         'score': {
    #             'required': 'スコアが入力されていません'
    #         },
    #         'level': {
    #             'required': 'レベルが入力されていません'
    #         },
    #         'time': {
    #             'required': '入力時間が入力されていません'
    #         },
    #         'count': {
    #             'required': '入力文字数が入力されていません'
    #         },
    #         'miss': {
    #             'required': 'ミス入力数が入力されていません'
    #         },
    #         'read': {
    #             'required': 'WPMが入力されていません'
    #         },
    #         'rate': {
    #             'required': '正確率が入力されていません'
    #         },
    #         'weakness': {
    #             'required': '苦手キーが入力されていません'
    #         },
    #     }

    # def clean(self):
    #     if self.cleaned_data.get('name') == "":
    #         raise forms.ValidationError('No name!')
    #     return self.cleaned_data


class form(forms.Form):
    user_id = forms.IntegerField(required=True, initial=1)
    name = forms.CharField(required=True, max_length=30)
    date = forms.DateField(required=True)
    course = forms.ChoiceField(required=True, initial=200)
    score = forms.IntegerField(required=True)
    level = forms.CharField(required=True, max_length=30)
    time = forms.TimeField(required=True)
    count = forms.IntegerField(required=True)
    miss = forms.IntegerField(required=True)
    read = forms.DecimalField(required=True, max_digits=5, decimal_places=2)
    rate = forms.IntegerField(required=True)
    weakness = forms.IntegerField(required=False)
