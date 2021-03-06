# Generated by Django 3.1.1 on 2020-10-29 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batsmen_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRST_NAME', models.CharField(max_length=50)),
                ('LAST_NAME', models.CharField(max_length=50)),
                ('COUNTRY', models.CharField(max_length=50)),
                ('AGE', models.IntegerField()),
                ('RUNS', models.IntegerField()),
                ('AVG', models.FloatField()),
                ('RANK', models.IntegerField()),
                ('PLAYED', models.IntegerField()),
                ('STR', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Batsmen_info',
                'verbose_name_plural': 'Batsmen_infos',
            },
        ),
    ]
