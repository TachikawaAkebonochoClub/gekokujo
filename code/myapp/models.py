from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(
        verbose_name='名前',
        max_length=200
    )
    class Meta:
        ordering = ('id',)
