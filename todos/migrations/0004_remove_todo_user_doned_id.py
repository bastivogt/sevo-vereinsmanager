# Generated by Django 5.0.6 on 2024-05-30 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_todo_user_doned_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user_doned_id',
        ),
    ]