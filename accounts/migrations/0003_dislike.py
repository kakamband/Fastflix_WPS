# Generated by Django 2.2.3 on 2019-07-10 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20190710_1658'),
        ('accounts', '0002_remove_subuser_dislike'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislike', to='movies.Movie')),
                ('sub_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislike', to='accounts.SubUser')),
            ],
        ),
    ]
