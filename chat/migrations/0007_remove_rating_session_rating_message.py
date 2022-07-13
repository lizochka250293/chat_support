# Generated by Django 4.0.5 on 2022-07-13 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_rating_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='session',
        ),
        migrations.AddField(
            model_name='rating',
            name='message',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='chat.numberview', verbose_name='сообщение'),
        ),
    ]