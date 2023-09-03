# Generated by Django 4.2.4 on 2023-09-03 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('pages', models.IntegerField()),
                ('year', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('genre', models.CharField(max_length=50)),
                ('auther', models.CharField(max_length=25)),
                ('bio', models.TextField()),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
