# Generated by Django 2.2.3 on 2019-08-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190805_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='subuser',
            name='is_initialize',
            field=models.BooleanField(default=False),
        ),
    ]
