# Generated by Django 4.0.5 on 2022-07-19 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_ratingstar_value_alter_rating_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='rating',
            name='star_1',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='star_1', to='chat.ratingstar', verbose_name='звезда_1'),
        ),
        migrations.AddField(
            model_name='rating',
            name='star_2',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='star_2', to='chat.ratingstar', verbose_name='звезда_2'),
        ),
        migrations.AlterField(
            model_name='ratingstar',
            name='value',
            field=models.PositiveSmallIntegerField(choices=[(1, 'одна звезда'), (2, 'две звезды'), (3, 'три звезды'), (4, 'четыре звезды'), (5, 'пять звезд')], default=1, verbose_name='значение'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('star_1', 'star_2', 'message')},
        ),
        migrations.RemoveField(
            model_name='rating',
            name='star',
        ),
    ]
