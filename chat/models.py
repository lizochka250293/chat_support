from django.db import models


class Number(models.Model):
    number = models.CharField('number', max_length=70)
    message = models.TextField('message', max_length=200)
    #session = models.TextField('sessoin', default='1', max_length=200)
    date = models.DateTimeField('time', auto_now_add=True)


class NumberView(models.Model):
    numberview = models.CharField('number', max_length=70)
    messageview = models.TextField('message', max_length=200)
    sessionview = models.TextField('sessoin', default='1', max_length=200)
    dateview = models.DateTimeField('time', auto_now_add=True)

class StarChoises(models.IntegerChoices):
    ONE=1, 'одна звезда'
    TWO =2, 'две звезды'
    THREE =3, 'три звезды'
    FOUR =4, 'четыре звезды'
    FIFE =5, 'пять звезд'

class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField('значение', default=StarChoises.ONE, choices=StarChoises.choices)

    def __str__(self):
        return f'{self.value}'

class Rating(models.Model):
    number = models.ForeignKey(Number, on_delete=models.CASCADE, verbose_name='пользователь', default='1', related_name='user_ratings')
    star_1 = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда_1', related_name='star_1', default='1')
    star_2 = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда_2', related_name='star_2', default='1')
    message = models.ForeignKey(NumberView, on_delete=models.CASCADE, verbose_name='сообщение', default='1')
    comment = models.TextField('комментарии', max_length=200, blank=True)
    admin_number = models.ForeignKey(Number, on_delete=models.CASCADE, verbose_name='пользователь_админ', default='1', related_name='admin_ratings')

    class Meta:

        unique_together = ('star_1', 'star_2', 'message')

    def __str__(self):
        return f'{self.star_1} \n {self.star_2} \n {self.message}'


