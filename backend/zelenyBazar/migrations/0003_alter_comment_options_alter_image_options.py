# Generated by Django 4.1.3 on 2022-11-27 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zelenyBazar', '0002_alter_comment_parentcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'managed': True},
        ),
    ]
