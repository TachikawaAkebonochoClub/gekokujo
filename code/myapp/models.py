from django.db import models
from django.core import validators

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(
        verbose_name='名前',
        max_length=200
    )
    age = models.CharField(
        verbose_name='年齢',
        max_length=50, 
        blank=True,null=True
    )
    gender = models.CharField(
        verbose_name='性別',
        max_length=200, 
        blank=True,null=True
    )
    stature = models.CharField(
        verbose_name='身長',
        max_length=200, 
        blank=True,null=True
    )
    birthday = models.CharField(
        verbose_name='誕生日',
        max_length=50, 
        blank=True,null=True
    )
    class Meta:
        ordering = ('id',)
