# Generated by Django 4.0.5 on 2022-07-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number1', models.CharField(max_length=70, verbose_name='number')),
                ('message1', models.TextField(max_length=200, verbose_name='message')),
                ('date1', models.DateTimeField(auto_now_add=True, verbose_name='time')),
            ],
        ),
    ]
