# Generated by Django 2.2.4 on 2019-08-31 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='blog',
        ),
    ]
