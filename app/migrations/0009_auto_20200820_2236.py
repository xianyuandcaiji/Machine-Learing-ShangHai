# Generated by Django 2.2.14 on 2020-08-20 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200820_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_list',
            name='is_top',
            field=models.BooleanField(default=False),
        ),
    ]