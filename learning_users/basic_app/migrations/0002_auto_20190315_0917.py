# Generated by Django 2.1.7 on 2019-03-15 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='opt_news',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='prof_desig',
            field=models.TextField(blank=True),
        ),
    ]
