# Generated by Django 4.0.3 on 2022-06-20 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
    ]
