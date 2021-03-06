# Generated by Django 3.0.4 on 2020-04-02 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_auto_20200329_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('start_year', models.IntegerField()),
                ('start_month', models.IntegerField(choices=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')])),
                ('end_year', models.IntegerField(blank=True, null=True)),
                ('end_month', models.IntegerField(blank=True, choices=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')], null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='education',
            name='end_month',
            field=models.IntegerField(blank=True, choices=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')], null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_month',
            field=models.IntegerField(choices=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')]),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_month',
            field=models.IntegerField(blank=True, choices=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')], null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='start_month',
            field=models.IntegerField(choices=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')]),
        ),
    ]
