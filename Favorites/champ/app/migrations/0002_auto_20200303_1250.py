# Generated by Django 3.0.2 on 2020-03-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='example@gmail.com', max_length=254),
        ),
    ]