# Generated by Django 3.0.4 on 2020-03-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techskills',
            name='year_exp',
            field=models.IntegerField(),
        ),
    ]
