# Generated by Django 2.2 on 2019-04-22 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='com',
            new_name='post',
        ),
    ]
