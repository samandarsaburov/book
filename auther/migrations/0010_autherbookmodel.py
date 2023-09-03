# Generated by Django 4.2.4 on 2023-09-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auther', '0009_alter_authermodel_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutherBookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('pages', models.IntegerField()),
                ('year', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('images', models.ImageField(default='', upload_to='images/')),
                ('bio', models.TextField()),
                ('genre', models.CharField(choices=[('Adventure', 'Adventure'), ('Science Fiction', 'Science Fiction'), ('Romance', 'Romance')], max_length=50)),
            ],
            options={
                'db_table': 'autherbook',
            },
        ),
    ]
