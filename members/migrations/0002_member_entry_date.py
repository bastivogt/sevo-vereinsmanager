# Generated by Django 5.0.6 on 2024-05-28 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='entry_date',
            field=models.DateField(null=True),
        ),
    ]
