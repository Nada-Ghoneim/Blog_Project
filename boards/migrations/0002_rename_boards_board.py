# Generated by Django 5.1 on 2024-08-26 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Boards',
            new_name='Board',
        ),
    ]
