from django.db import models
from django.core import validators
from django.utils import timezone

# Create your models here.

class ScoreTable(models.Model):

    courses = (
    (100,'おやじギャグ'),
    (200,'お嬢様ことば'),
    (300,'早口ことば'),
    (400,'回文'),
    (500,'缶コーヒーのコピー'),
    (600,'時代劇のセリフ'),
    (700,'元気が出ることば'),
    (800,'アニメタイトル'),
    )

    id = models.AutoField(
        verbose_name='record_id',
        primary_key=True
    )
    user_id = models.IntegerField(
        verbose_name='user_id',
        default=1,
    )
    name = models.CharField(
        verbose_name='イニシャル',
        max_length=30
    )
    date = models.DateField(
        verbose_name='実施日',
        default=timezone.now
    )
    course = models.IntegerField(
        verbose_name='コース',
        choices=courses,
        default=200
    )
    score = models.IntegerField(
        verbose_name='スコア'
    )
    level = models.CharField(
        verbose_name='レベル',
        max_length=30
    )
    time = models.TimeField(
        verbose_name='入力時間',
    )
    count = models.IntegerField(
        verbose_name='入力文字数',
        validators=[validators.MinValueValidator(1)]
    )
    miss = models.IntegerField(
        verbose_name='ミス入力数'
    )
    read = models.DecimalField(
        verbose_name='WPM',
        max_digits=5,decimal_places=2
    )
    rate = models.DecimalField(
        verbose_name='正確率',
        max_digits=5,
        decimal_places=2,
        validators=[validators.MinValueValidator(0.01),
        validators.MaxValueValidator(100.00)]
    )
    weakness = models.CharField(
        verbose_name='苦手キー',
        max_length=10,
        blank=True,
        null=True
    )
