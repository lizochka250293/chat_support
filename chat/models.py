from django.db import models


class Number(models.Model):
    number = models.CharField('number', max_length=70)
    message = models.TextField('message', max_length=200)
    session = models.TextField('sessoin', default='1', max_length=200)
    date = models.DateTimeField('time', auto_now_add=True)


class NumberView(models.Model):
    numberview = models.CharField('number', max_length=70)
    messageview = models.TextField('message', max_length=200)
    sessionview = models.TextField('sessoin', default='1', max_length=200)
    dateview = models.DateTimeField('time', auto_now_add=True)
class StarChoises(models.IntegerChoices):
    ONE=1, 'одна звезда'
    TWO =2, 'две здезды'
    THREE =3, 'три здезды'
    FOUR =4, 'четыре здезды'
    FIFE =5, 'пять здезды'

class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField('значение', default=StarChoises.ONE, choices=StarChoises.choices)

    def __str__(self):
        return f'{self.value}'

class Rating(models.Model):
    number = models.CharField('number', max_length=70)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    message = models.ForeignKey(NumberView, on_delete=models.CASCADE, verbose_name='сообщение', default='1')
    comment = models.TextField('комментарии', max_length=200, blank=True)

    class Meta:

        unique_together = ('star', 'message')

    def __str__(self):
        return f'{self.star} - {self.message}'


