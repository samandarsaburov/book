# Generated by Django 4.2.4 on 2023-09-03 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='images',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]