# Generated by Django 3.0.4 on 2020-03-31 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_auto_20200331_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_month',
            field=models.CharField(blank=True, choices=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_month',
            field=models.CharField(choices=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')], max_length=3),
        ),
        migrations.AlterField(
            model_name='projectexperience',
            name='end_month',
            field=models.CharField(blank=True, choices=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='projectexperience',
            name='start_month',
            field=models.CharField(choices=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')], max_length=3),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_month',
            field=models.CharField(blank=True, choices=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='start_month',
            field=models.CharField(choices=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')], max_length=3),
        ),
    ]
