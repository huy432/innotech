# Generated by Django 4.2.1 on 2023-05-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]