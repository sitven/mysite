# Generated by Django 2.0 on 2019-08-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190811_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='reder_num',
            field=models.IntegerField(default=0),
        ),
    ]