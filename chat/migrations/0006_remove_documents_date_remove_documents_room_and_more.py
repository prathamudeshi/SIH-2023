# Generated by Django 4.2.5 on 2023-09-23 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_documents_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='date',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='room',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='user',
        ),
    ]