# Generated by Django 4.0.2 on 2022-02-10 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachersapplication', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.BigIntegerField(default=10),
        ),
    ]