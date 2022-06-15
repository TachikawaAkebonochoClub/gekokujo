# Generated by Django 2.1.3 on 2022-06-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='年齢'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='birthday',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='誕生日'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='性別'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='stature',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='身長'),
        ),
    ]