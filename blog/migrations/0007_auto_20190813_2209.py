# Generated by Django 2.0 on 2019-08-13 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190812_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readnum',
            name='blog',
        ),
        migrations.DeleteModel(
            name='ReadNum',
        ),
    ]
