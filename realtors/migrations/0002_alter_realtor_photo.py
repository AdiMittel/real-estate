# Generated by Django 3.2.9 on 2021-12-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
