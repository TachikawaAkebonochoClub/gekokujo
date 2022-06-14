from django import forms
from . models import UserInfo
 
class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('name','age','gender','stature','birthday')
        labelds={
            'name':'名前',
            'age':'年齢',
            'gender':'性別',
            'stature':'身長',
            'birthday':'誕生日',
            }
