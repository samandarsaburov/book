# Generated by Django 4.2.4 on 2023-09-03 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auther', '0006_alter_authermodel_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authermodel',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[('Adventure', 'Adventure'), ('Science Fiction', 'Science Fiction'), ('Romance', 'Romance')], max_length=50),
        ),
    ]
