from django.contrib.auth.models import AbstractUser
from django.db import models


# class Number(models.Model):
#     number = models.CharField('number', max_length=70)
#     message = models.TextField('message', max_length=200)
#     #session = models.TextField('sessoin', default='1', max_length=200)
#     date = models.DateTimeField('time', auto_now_add=True)
#
#
# class NumberView(models.Model):
#     numberview = models.CharField('number', max_length=70)
#     messageview = models.TextField('message', max_length=200)
#     sessionview = models.TextField('sessoin', default='1', max_length=200)
#     dateview = models.DateTimeField('time', auto_now_add=True)

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

    class Meta:
        verbose_name = 'Звезда'
        verbose_name_plural = 'Звезды'


class User(AbstractUser):

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'user'

class Chat_dialog(models.Model):
    start_date = models.DateTimeField('Дата создания', auto_now=True)

    def __str__(self):
        return f'{self.start_date}'

    class Meta:
        verbose_name = 'Диалог'
        verbose_name_plural = 'Диалоги'


class ChatMessage(models.Model):
    author = models.IntegerField('пользователь')
    dialog = models.ForeignKey(Chat_dialog, on_delete=models.CASCADE, verbose_name='диалог', related_name='dialog_chat')
    create_at = models.DateTimeField('Дата', auto_now=True)
    body = models.TextField('Текст обращения')

    def __str__(self):
        return f'{self.author} - {self.body}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Rating(models.Model):
    message = models.ForeignKey(ChatMessage, on_delete=models.CASCADE, verbose_name='сообщение', related_name='message_rating')
    star_1 = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда_1', related_name='star_1', default='1')
    star_2 = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда_2', related_name='star_2', default='1')
    star_3 = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда_3', related_name='star_3', default='1')
    rated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='пользователь', related_name="user_rating")
    comment = models.TextField('комментарии', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        unique_together = ('star_1', 'star_2', 'message')

    def __str__(self):
        return f'{self.star_1} \n {self.star_2} \n {self.star_3}'


