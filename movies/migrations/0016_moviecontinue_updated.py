# Generated by Django 2.2.3 on 2019-07-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_auto_20190730_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviecontinue',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]