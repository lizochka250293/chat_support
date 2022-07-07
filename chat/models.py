from django.db import models


class Number(models.Model):
    number = models.CharField('number', max_length=70)
    message = models.TextField('message', max_length=200)
    date = models.DateTimeField('time', auto_now_add=True)

