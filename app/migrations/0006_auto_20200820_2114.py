# Generated by Django 2.2.14 on 2020-08-20 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_article_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_list',
            name='like_numb',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article_list',
            name='read_numb',
            field=models.IntegerField(default=0),
        ),
    ]
